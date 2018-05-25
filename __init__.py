import argparse;


def main():
    parser = argparse.ArgumentParser(description='Stackoverflow data dump XML parser.')

    parser.add_argument('--file',
                        help='pass the file to parse the xml')
    parser.add_argument('--delimiter', help='delimiter in the file')

    args = parser.parse_args()
    print(args.file)

   # if args:
#        if args.file:


main()