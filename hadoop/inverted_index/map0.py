#!/usr/bin/env python3
"""Map 0."""

import csv
import sys

csv.field_size_limit(sys.maxsize)
total_docs = 0
# Process each line from CSV
for row in csv.reader(sys.stdin):
    doc_id, doc_title, doc_body = row
    label = "doc_info"
    print(f"{label}\t{doc_id} {doc_title} {doc_body}")
