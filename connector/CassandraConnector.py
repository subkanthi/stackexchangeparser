from cassandra.cluster import Cluster

class CassandraConnector:

    def __init__(self, ipAddress, keySpace):
        print("CassandraConnector constructor")
        self.ipAddress = ipAddress
        self.keyspace = keySpace

    def connect(self):
        self.cluster = Cluster(self.ipAddress)
        if self.cluster is None:
            if self.keyspace is None:
                self.cluster.connect(self.keyspace)
            else:
                self.cluster.connect()

    

