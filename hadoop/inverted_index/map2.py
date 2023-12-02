#!/usr/bin/env python3
"""Map 2."""
import csv
import math
import os
import re
import sys

# Compute document frequencies
for line in sys.stdin:
    doc_id, word, frequency = line.strip().split()
    print(f"{word}\t{doc_id} {frequency}")
