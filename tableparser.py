#!/usr/bin/python

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--htmltable', required=True)

args = parser.parse_args()

def gettable(tablepath):
	with open(tablepath) as table:
		return table.read()

htmltable = gettable(args.htmltable)

tablelist = re.findall(r'\<table.*?/table\>*?',htmltable)

print(tablelist)
print(f"Total available table {len(tablelist)}")

