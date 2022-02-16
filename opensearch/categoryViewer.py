import sys
import os
import xml.etree.ElementTree as ET

# Location for category data
categoriesFilename = '/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

maxDepth = int(sys.argv[1]) if (len(sys.argv) >- 2) else 0
tree = ET.parse(categoriesFilename)
root = tree.getroot()

catPathStrs = set()

for child in root:
    catPath = child.find('path')
    catPathStr = ''
    depth = 0
    for cat in catPath:
        if catPathStr != '':
            catPathStr += ' > '
        catPathStr += cat.find('name').text
        depth += 1
        catPathStrs.add(catPathStr)
        if maxDepth > 0 and depth == maxDepth:
            break

# Sort for readability
for catPathStr in sorted(catPathStrs):
    print(catPathStr)
