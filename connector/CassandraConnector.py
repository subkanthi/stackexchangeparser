from cassandra.cluster import Cluster
import logging

class CassandraConnector:

    def __init__(self, ipAddress, keySpace):
        self._logger = logging.getLogger()
        self._logger.debug("CassandraConnector constructor")
        self._ipAddress__ = ipAddress
        self._keyspace = keySpace

    def connect(self):
        self._cluster = Cluster([self._ipAddress])
        if self._cluster is not None:
            if self._keyspace is None:
                self._session = self.cluster.connect(self._keyspace)
            else:
                self._session = self.cluster.connect()
        else:
            self._logger.debug("error creating cassandra cluster")


    def writeData(self):
        if self._session is not None:
            #self.session.execute("use keyspace " + self.keyspace);
            self._session.execute("INSERT INTO stackoverflow.comments (name, age) VALUES (%s, %s)", ("bob", 42))
        else:
            self._logger.debug("error creating cassandra session")