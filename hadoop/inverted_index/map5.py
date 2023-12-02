#!/usr/bin/env python3
"""Map 5."""
import csv
import math
import os
import re
import sys

# Compute normalization factors
# Normalization factor = sum((tf * idf) ** 2) for all terms in doc
# get doc count from total_document_count.txt
for line in sys.stdin:
    doc_mod = line.strip().split()[0]
    text = line.partition("\t")[2]
    text = text.strip("\n")
    # Must use doc_id % 3 as key for reducer
    # print(f"{word}\t{idf} {doc_id} {tf} {norm_factor}")
    print(f"{doc_mod}\t{text}")
