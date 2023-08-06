"""DB-API implementation backed by HiveServer2 (Thrift API)
See http://www.python.org/dev/peps/pep-0249/
Many docstrings in this file are based on the PEP, which is in the public domain.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import datetime
# Make all exceptions visible in this e6xdb per DB-API
import logging
import re
import sys
from decimal import Decimal
from io import BytesIO
from ssl import CERT_NONE, CERT_OPTIONAL, CERT_REQUIRED

from e6xdb.server import QueryEngineService
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from e6xdb.common import DBAPITypeObject, ParamEscaper, DBAPICursor
from e6xdb.constants import *
from e6xdb.datainputstream import DataInputStream, get_query_columns_info, read_rows_from_batch, read_values_from_array
from e6xdb.typeId import *

apilevel = '2.0'
threadsafety = 2  # Threads may share the e6xdb and connections.
paramstyle = 'pyformat'  # Python extended format codes, e.g. ...WHERE name=%(name)s
key = b"teamuniphi@cunninghamroadfrmbang"

_logger = logging.getLogger(__name__)

_TIMESTAMP_PATTERN = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+(\.\d{,6})?)')

ssl_cert_parameter_map = {
    "none": CERT_NONE,
    "optional": CERT_OPTIONAL,
    "required": CERT_REQUIRED,
}


def _parse_timestamp(value):
    if value:
        match = _TIMESTAMP_PATTERN.match(value)
        if match:
            if match.group(2):
                format = '%Y-%m-%d %H:%M:%S.%f'
                # use the pattern to truncate the value
                value = match.group()
            else:
                format = '%Y-%m-%d %H:%M:%S'
            value = datetime.datetime.strptime(value, format)
        else:
            raise Exception(
                'Cannot convert "{}" into a datetime'.format(value))
    else:
        value = None
    return value


TYPES_CONVERTER = {"DECIMAL_TYPE": Decimal,
                   "TIMESTAMP_TYPE": _parse_timestamp}


class HiveParamEscaper(ParamEscaper):
    def escape_string(self, item):
        # backslashes and single quotes need to be escaped
        # TODO verify against parser
        # Need to decode UTF-8 because of old sqlalchemy.
        # Newer SQLAlchemy checks dialect.supports_unicode_binds before encoding Unicode strings
        # as byte strings. The old version always encodes Unicode as byte strings, which breaks
        # string formatting here.
        if isinstance(item, bytes):
            item = item.decode('utf-8')
        return "'{}'".format(
            item
            .replace('\\', '\\\\')
            .replace("'", "\\'")
            .replace('\r', '\\r')
            .replace('\n', '\\n')
            .replace('\t', '\\t')
        )


_escaper = HiveParamEscaper()


def connect(*args, **kwargs):
    """Constructor for creating a connection to the database. See class :py:class:`Connection` for
    arguments.
    :returns: a :py:class:`Connection` object.
    """
    return Connection(*args, **kwargs)


class Connection(object):
    """Wraps a http e6xdb session"""

    def __init__(
            self,
            host=None,
            port=None,
            scheme=None,
            username=None,
            database='default',
            auth=None,
            configuration=None,
            kerberos_service_name=None,
            password=None,
            check_hostname=None,
            ssl_cert=None,
            thrift_transport=None
    ):
        username = username
        password = password
        self.database = database
        scheme = "e6xdb"
        # service_name = 'E6x'  # E6x  QueryExecutor
        service_name = 'QueryEngine'  # E6x  QueryExecutor

        if scheme != "e6xdb":
            raise ValueError("scheme is not e6xdb")

        if password is None:
            raise ValueError("Password should be set")

        if port is None:
            port = 9000
        self._transport = TSocket.TSocket(host, port)
        self._transport = TTransport.TBufferedTransport(self._transport)

        protocol = TBinaryProtocol.TBinaryProtocol(self._transport)
        protocol = TMultiplexedProtocol.TMultiplexedProtocol(protocol, service_name)
        self._client = QueryEngineService.Client(protocol)
        self._transport.open()

        try:
            authSession = self._client.authenticate(username, password)
            if not authSession:
                raise ValueError("invalid username or password")
            # self._client.setSchema(database)
        except Exception as e:
            self._transport.close()
            raise e

    def __enter__(self):
        """Transport should already be opened by __init__"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Call close"""
        self.close()

    def close(self):
        self._transport.close()

    def check_connection(self):
        return self._transport.isOpen()

    def clear(self, query_id):
        self._client.clear(query_id)

    def reopen(self):
        self._transport.close()
        self._transport.open()

    def query_cancel(self, query_id):
        self._client.cancelQuery(queryId=query_id)

    def get_tables(self, database):
        return self._client.getTables(schema=database)

    def getTables(self, database):
        return self.get_tables(database)

    def get_columns(self, database, table):
        return self._client.getColumns(schema=database, table=table)

    def getColumns(self, database, table):
        return self.get_columns(database, table)

    def get_schema_names(self):
        return self._client.getSchemaNames()

    def commit(self):
        """Hive does not support transactions, so this does nothing."""
        pass

    def cursor(self, *args, **kwargs):
        """Return a new :py:class:`Cursor` object using the connection."""
        return Cursor(self, *args, **kwargs)

    def rollback(self):
        raise Exception("e6xdb does not support transactions")  # pragma: no cover

    @property
    def client(self):
        return self._client


class Cursor(DBAPICursor):
    """These objects represent a database cursor, which is used to manage the context of a fetch
    operation.
    Cursors are not isolated, i.e., any changes done to the database by a cursor are immediately
    visible by other cursors or connections.
    """
    rows_count = 0

    def __init__(self, connection, arraysize=1000):
        super(Cursor, self).__init__()
        self._arraysize = arraysize
        self.connection = connection
        self._data = None
        self._query_columns_description = None
        self._is_metadata_updated = False
        self._description = None
        self._query_id = None
        self._batch = list()
        self._rowcount = 0
        self._database = self.connection.database

    def _reset_state(self):
        """Reset state about the previous query in preparation for running another query"""
        pass

    @property
    def arraysize(self):
        return self._arraysize

    @arraysize.setter
    def arraysize(self, value):
        """Array size cannot be None, and should be an integer"""
        default_arraysize = 1000
        try:
            self._arraysize = int(value) or default_arraysize
        except TypeError:
            self._arraysize = default_arraysize

    @property
    def description(self):
        """This read-only attribute is a sequence of 7-item sequences.
        Each of these sequences contains information describing one result column:
        - name
        - type_code
        - display_size (None in current implementation)
        - internal_size (None in current implementation)
        - precision (None in current implementation)
        - scale (None in current implementation)
        - null_ok (always True in current implementation)
        This attribute will be ``None`` for operations that do not return rows or if the cursor has
        not had an operation invoked via the :py:meth:`execute` method yet.
        The ``type_code`` can be interpreted by comparing it to the Type Objects specified in the
        section below.
        """
        if self._description is None:
            self._description = []
            for col in self._query_columns_description:
                type_code = col.get_field_type()
                column_name = col.get_name()
                self._description.append((
                    column_name,
                    type_code,
                    None, None, None, None, True
                ))
        return self._description

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close the operation handle"""
        self.connection.close()
        self._arraysize = None
        self.connection = None
        self._data = None
        self._query_columns_description = None
        self._description = None
        self._query_id = None
        self._batch = None
        self._rowcount = None
        self._database = None

    def get_tables(self):
        schema = self.connection.database
        return self.connection.get_tables(database=schema)

    def get_columns(self, table):
        schema = self.connection.database
        return self.connection.get_columns(database=schema, table=table)

    def clear(self):
        """Clears the tmp data"""
        self.connection.clear(self._query_id)

    def cancel(self, query_id):
        _logger.info("Cancelling query")
        self.connection.query_cancel(query_id)

    def execute(self, operation, parameters=None, **kwargs):
        """Prepare and execute a database operation (query or command).
        Return values are not defined.
        """
        """
        Semicolon is now not supported. So removing it from query end.
        """
        if operation.endswith(';'):
            operation = operation[:-1]

        # Prepare statement
        if parameters is None:
            sql = operation
        else:
            sql = operation % _escaper.escape_args(parameters)

        client = self.connection.client
        self._query_id = client.prepareStatement(
            self._database,
            sql
        )
        client.executeStatement(self._query_id)

        # _logger.info("getting result metadata")
        self.update_mete_data()
        # _logger.info("finished populating metadata", self._query_id)
        return self._query_id

    def rowcount(self):
        # _logger.info("fetch returning the rowcount from e6x itself")
        return self._rowcount

    def update_mete_data(self):
        buffer = self.connection.client.getResultMetadata(self._query_id)
        buffer = BytesIO(buffer)
        self._rowcount, self._query_columns_description = get_query_columns_info(buffer)

    def _fetch_more(self):
        # _logger.info("fetching batch")
        batch_size = self._arraysize
        self._data = list()
        for i in range(batch_size):
            rows = self.fetch_batch()
            if rows is None:
                return
            self._data = self._data + rows

        # _logger.info("fetched batch of {num}".format(num=len(self._data)))
        return self._data

    def _fetch_all(self):
        self._data = list()
        while True:
            rows = self.fetch_batch()
            if rows is None:
                break
            self._data = self._data + rows
        rows = self._data
        self._data = None
        return rows

    def fetch_batch(self):
        # _logger.debug("fetching next batch from e6data")
        client = self.connection.client
        buffer = client.getNextResultBatch(self._query_id)
        if not self._is_metadata_updated:
            self.update_mete_data()
            self._is_metadata_updated = True
        if not buffer:
            return None
        buffer = BytesIO(buffer)
        dis = DataInputStream(buffer)
        # one batch retrieves the predefined set of rows
        return read_rows_from_batch(self._query_columns_description, dis)

    def fetchall(self):
        return self._fetch_all()

    def fetchmany(self, size=None):
        # _logger.info("fetching all from overriden method")
        if size is None:
            size = self.arraysize
        if self._data is None:
            self._data = list()
        while len(self._data) < size:
            # _logger.info("fetching next batch from fetch many")
            rows = self.fetch_batch()
            if rows is None:
                break
            self._data += rows
        _logger.info(len(self._data))
        if len(self._data) <= size:
            rows = self._data
            self._data = None
            return rows
        rows = self._data[:size]
        self._data = self._data[size:]
        return rows

    def fetchone(self):
        # _logger.info("fetch One returning the batch itself which is limited by predefined no.of rows")
        rows_to_return = []
        client = self.connection.client
        buffer = client.getNextResultRow(self._query_id)
        if not self._is_metadata_updated:
            self.update_mete_data()
            self._is_metadata_updated = True
        if not buffer:
            return None
        buffer = BytesIO(buffer)
        dis = DataInputStream(buffer)
        rows_to_return.append(read_values_from_array(self._query_columns_description, dis))
        return rows_to_return

    def explain(self):
        return self.connection.client.explain(self._query_id)

    def explain_analyse(self):
        return self.connection.client.explainAnalyze(self._query_id)


def poll(self, get_progress_update=True):
    """Poll for and return the raw status data provided by the Hive Thrift REST API.
    :returns: ``ttypes.TGetOperationStatusResp``
    :raises: ``ProgrammingError`` when no query has been started
    .. note::
        This is not a part of DB-API.
    """
    pass


def fetch_logs(self):
    """Retrieve the logs produced by the execution of the query.
    Can be called multiple times to fetch the logs produced after the previous call.
    :returns: list<str>
    :raises: ``ProgrammingError`` when no query has been started
    .. note::
        This is not a part of DB-API.
    """
    pass


class Error(Exception):
    pass

#
# Type Objects and Constructors
#

for type_id in PRIMITIVE_TYPES:
    name = TypeId._VALUES_TO_NAMES[type_id]
    setattr(sys.modules[__name__], name, DBAPITypeObject([name]))


if __name__ == '__main__':
    host = '127.0.0.1'
    e6x_connection = connect(
        host=host,
        port=9000,
        scheme="e6xdb",
        username="admin",
        database="tpcds_ci",
        auth=None,
        configuration=None,
        kerberos_service_name=None,
        password="admin",
        check_hostname=None,
        ssl_cert=None,
        thrift_transport=None
    )
    print('Connected.')
    import time

    start = time.time()
    cursor = e6x_connection.cursor()

    query = 'select * from date_dim limit 2'
    query_id = cursor.execute(query)
    print('query_id', query_id)
    all_records = cursor.fetchall()
    print(time.time() - start)
    for record in all_records:
        print(all_records)
    print(cursor.explain_analyse())
    e6x_connection.close()
#
#     e6x_connection.reopen()
#
#     cursor = e6x_connection.cursor()
#     query = 'SELECT * FROM date_dim limit 4;'
#     cursor.execute(query)
#     all_records = cursor.fetchall()
#     print(all_records)
#     # cursor.close()
#
#     e6x_connection.close()


