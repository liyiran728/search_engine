#!/usr/bin/env python3
"""Reduce3."""
import sys
import itertools


# Print inverted index
def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    norm_factor = 0
    for line in group:
        _, word, tf, idf = line.strip().split()
        norm_factor += ((float(tf) * float(idf)) ** 2)

    for line in group:
        doc_id, word, tf, idf = line.strip().split()
        print(f"{doc_id}\t{word} {tf} {idf} {norm_factor}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
