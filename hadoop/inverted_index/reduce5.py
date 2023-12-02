#!/usr/bin/env python3
"""Reduce5."""
import sys
import itertools
import math


def reduce_one_group(key, group):
    """Reduce one group."""
    for line in group:
        text = line.partition("\t")[2]
        text = text.strip("\n")
        print(f"{text}")
    # docs = {}
    # for line in group:
        # key, idf, doc_id, tf, norm_factor = line.strip().split()
        # if key in docs:
        #   docs[key].append([doc_id, tf, norm_factor])
        # else:
        #   docs[key] = [[doc_id, tf, norm_factor]]
    # text = ""
    # for i in range(len(docs[key])):
        # info = ' '.join(docs[key][i])
        # text = text + " " + info
    # print(f"{key}\t{idf}{text}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
