#!/usr/bin/env python3
"""Reduce4."""
import sys
import itertools
import math


def reduce_one_group(key, group):
    """Reduce one group."""
    # for line in group:
    #   _, word, idf, doc_id, tf, norm_factor = line.strip().split()
    #  print(f"{word} {idf} {doc_id} {tf} {norm_factor}")

    docs = {}
    for line in group:
        doc_mod, word, idf, doc_id, tf, norm_factor = line.strip().split()
        if word in docs:
            docs[word].append([doc_id, tf, norm_factor])
        else:
            docs[word] = [[doc_id, tf, norm_factor]]
    text = ""
    for i in range(len(docs[key.split()[1]])):
        info = ' '.join(docs[key.split()[1]][i])
        text = text + " " + info
    print(f"{doc_mod}\t{word} {idf}{text}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
