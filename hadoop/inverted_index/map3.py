#!/usr/bin/env python3
"""Map 3."""
import csv
import math
import os
import re
import sys

# Compute normalization factors
# Normalization factor = sum((tf * idf) ** 2) for all terms in doc
# get doc count from total_document_count.txt
for line in sys.stdin:

    doc_id, word, tf, idf = line.strip().split()
    # Must use doc_id % 3 as key for reducer
    # print(f"{doc_id % 3}\t")
    print(f"{doc_id}\t{word} {tf} {idf}")
