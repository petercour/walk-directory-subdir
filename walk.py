# Collect files in directory and subdirectories
# python3 walk.py <DIRECTORY>

import os
import sys

fileList = []
rootdir = sys.argv[1]

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        fileList.append(os.path.join(root,file))

print(fileList)

