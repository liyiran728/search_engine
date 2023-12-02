#!/usr/bin/env python3
"""Reduce0."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    total = 0
    for line in group:
        total += 1
    print(f"{total}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
