#!/usr/bin/env python3
"""Reduce1."""
import sys
import itertools


# Take in cleaned input and compute term frequencies
def reduce_one_group(key, group):
    """Reduce one group."""
    # group = list(group)
    word_count = 0
    for line in group:
        _, _, count = line.strip().split()
        word_count += int(count)
    print(f"{key}\t{word_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
