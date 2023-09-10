import argparse
import os
import re


def main():
    parser = argparse.ArgumentParser(description='Process some documents')
    parser.add_argument('--text_file', type=str, required=True,
                        help='a text file containing documents')

    args = parser.parse_args()
    text_file = open(args.text_file, 'r')
    documents = text_file.read().split("\n\n")
    formatted_docs = []
    inverted_index = {}
    for doc in documents:
        formatted_docs.append(re.split(r'\s+|\d+|\W+', doc))
    for i in range(0, len(formatted_docs)):
        for word in formatted_docs[i]:
            inverted_index[word] = [i+1] if not inverted_index.get(word) else inverted_index[word] + [i+1]
    print(inverted_index)

    
main()