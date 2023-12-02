#!/usr/bin/env python3
"""Reduce2."""
import sys
import itertools
import re
import math


# Compute IDF
# IDF = float(math.log10(total_docs / df))
def reduce_one_group(key, group):
    """Reduce one group."""
    # get doc count from total_document_count.txt
    text_file = open("total_document_count.txt", "r")
    total_docs = text_file.read()
    text_file.close()

    total_docs = re.sub(r'\n^$', '', total_docs, flags=re.MULTILINE)
    total_docs = re.split('\n', total_docs)
    total_docs = float(total_docs[0])

    group = list(group)
    doc_count = 0
    docs = {}
    for line in group:
        doc_count += 1

    idf = float(math.log10(total_docs / doc_count))

    for line in group:
        word = key
        _, doc_id, tf = line.strip().split()
        print(f"{doc_id}\t{word} {tf} {idf}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
