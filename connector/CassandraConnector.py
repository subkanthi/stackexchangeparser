from cassandra.cluster import Cluster
import logging

class CassandraConnector:

    def __init__(self, ipAddress, keySpace):
        self.logger = logging.getLogger()
        self.logger.debug("CassandraConnector constructor")
        self.ipAddress = ipAddress
        self.keyspace = keySpace

    def connect(self):
        self.cluster = Cluster([self.ipAddress])
        if self.cluster is not None:
            if self.keyspace is None:
                self.session = self.cluster.connect(self.keyspace)
            else:
                self.session = self.cluster.connect()
        else:
            self.logger.debug("error creating cassandra cluster")


    def writeData(self):
        if self.session is not None:
            self.session.execute("INSERT INTO comments (name, age) VALUES (%s, %d)", ("bob", 42))
        else:
            self.logger.debug("error creating cassandra session")