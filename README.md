# CSVIndex
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV (indexed)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

A PluMA plugin that indexes a CSV file, selecting user-specified
columns and creating a new CSV file with only those columns.

The plugin takes as input a tab-separated file of two keyword value
pairs: csvfile (name of the input CSV file) and indexfile (txt file
with each index on a separate line).
