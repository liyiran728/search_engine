#!/usr/bin/env python3
"""Map 1."""
import csv
import math
import os
import re
import sys

# Clean Input in Map 1
# Read CSV from stdin
csv.field_size_limit(sys.maxsize)
text_file = open("stopwords.txt", "r")
stopwords = text_file.read()
text_file.close()

stopwords = re.sub(r'\n^$', '', stopwords, flags=re.MULTILINE)
li = re.split('\n', stopwords)

# Process each line from CSV
for row in csv.reader(sys.stdin):
    doc_id, doc_title, doc_body = row
    # print(f"{doc_id}\t{doc_title} {doc_body}")

    # Combine document title and body, separated by a space
    text = row[1] + " " + row[2]
    # Remove non alphanumeric characters
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    # Make all text lowercase
    text = text.casefold()
    # Split text into whitespace-delimited terms
    text = text.split()

    for word in list(text):
        if word in li:
            text.remove(word)
        else:
            print(f"{doc_id} {word}\t{1}")
