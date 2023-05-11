import os
import re

# define a regular expression for matching
pattern = r'^file\d+\.txt$'

# to match file names in a path
dir_path = '/path/to/folder'
file_names = os.listdir(dir_path)

# filter the files with the RE
matched_files = [f for f in file_names if re.match(pattern, f)]

# print
print(matched_files)