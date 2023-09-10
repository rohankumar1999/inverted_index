import sys
import os
import re


def main():
    text_file = open(sys.argv[1], 'r')
    documents = text_file.read().split("\n\n")
    formatted_docs = []
    inverted_index = {}
    for doc in documents:
        formatted_docs.append(re.split(r'\s+|\d+|\W+', doc))
    for i in range(0, len(formatted_docs)):
        for word in formatted_docs[i]:
            inverted_index[word] = {i+1} if not inverted_index.get(word) else inverted_index[word] | {i+1}
    inverted_index = dict(sorted(inverted_index.items()))
    line1 = ""
    num_words = "0000"+str(len(inverted_index))
    line1 += num_words[-4:]
    idx = 0
    for word in inverted_index.keys():
        line1 += ("0000"+str(idx))[-4:]
        idx += (len(word)+4)
    line2 = ""
    pos=0
    line3 = ""
    for word,docs in inverted_index.items():
        line2 += word
        line2 += ("0000"+str(pos))[-4:]
        pos += 2*len(docs)
        for doc in docs:
            line3+=(str(doc)+',')
    line3 = line3[:-1]
    print(line1)
    print(line2)
    print(line3)

main()
