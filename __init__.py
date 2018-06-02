import argparse;
import sys;
from XmlParser import XmlParser;
from connector.SparkConnector import  SparkConnector;
from connector.CassandraConnector import CassandraConnector;



def main():
    parser = argparse.ArgumentParser(description='Stackoverflow data dump XML parser.')
    parser.add_argument('--file',
                        help='pass the file to parse the xml')
    parser.add_argument('--delimiter', help='delimiter in the file')
    parser.add_argument('--cassandraIP', help='Cassandra DB IP address')
    parser.add_argument('--cassandraKeyspace', help='Cassandra Keyspace')


    args = parser.parse_args()

    if args.file is None:
        print(args.file)
        sys.exit(0)


    xmlParser = XmlParser(args.file)
    list = xmlParser.parseXml()
    #print(list.count())

    cassandraIP = args.cassandraIP
    cassandraKeyspace = args.cassandraKeyspace

    if cassandraIP is not None and cassandraKeyspace is not None:
        connector = CassandraConnector(cassandraIP, cassandraKeyspace)
    else:
        print(args.file)
        sys.exit(0)
        
    SparkConnector('s3n://sparkapache/Posts.xml')

main()