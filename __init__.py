import argparse;
from com.tfidf import FileParser
from com.tfidf import TermFrequency
from com.tfidf import InverseDocumentFrequency
from com.tfidf import TFIDF
from com.tfidf import EuclidianDistance

def main():
    parser = argparse.ArgumentParser(description='TF-IDF and Luigi pipeline.')

    parser.add_argument('--file',
                        help='pass the file to parse the text')
    parser.add_argument('--delimiter', help='delimiter in the file')

    args = parser.parse_args()
    print(args.file)

    if args:
        if args.file:
            array = FileParser.parseFileBasedOnDelimiter(args.file, args.delimiter)

            removedPunctuationArray = FileParser.removePunctuation(array)

            numberOfDocuments = removedPunctuationArray.__len__()

            termFrequencyDocuments = TermFrequency.calculateTermFrequency(removedPunctuationArray)

            inverseDocumentFrequency = InverseDocumentFrequency.calculateInverseDocumentFrequency(removedPunctuationArray, numberOfDocuments)

            tfIdfDocuments = TFIDF.calculateTfIdf(termFrequencyDocuments, inverseDocumentFrequency)

            EuclidianDistance.calculateSimilarityInDocuments(tfIdfDocuments)

main()