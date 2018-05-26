import argparse;
import sys;
from XmlParser import XmlParser;



def main():
    parser = argparse.ArgumentParser(description='Stackoverflow data dump XML parser.')
    parser.add_argument('--file',
                        help='pass the file to parse the xml')
    parser.add_argument('--delimiter', help='delimiter in the file')


    args = parser.parse_args()

    if args.file is None:
        print(args.file)
        sys.exit(0)


    xmlParser = XmlParser(args.file)
    list = xmlParser.parseXml()
    print(list.count())

main()