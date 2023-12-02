#!/usr/bin/env python3
"""Map 4."""
import csv
import math
import os
import re
import sys

# Compute normalization factors
# Normalization factor = sum((tf * idf) ** 2) for all terms in doc
# get doc count from total_document_count.txt
for line in sys.stdin:
    doc_id, word, tf, idf, norm_factor = line.strip().split()
    # Must use doc_id % 3 as key for reducer
    # print(f"{word}\t{idf} {doc_id} {tf} {norm_factor}")
    print(f"{int(doc_id) % 3} {word} {idf}\t{doc_id} {tf} {norm_factor}")
