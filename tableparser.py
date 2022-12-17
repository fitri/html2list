#!/usr/bin/python

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--htmltable', required=True)

args = parser.parse_args()

def gettable(tablepath):
	with open(tablepath) as table:
		return table.read()

#call function with passed arg
htmltable = gettable(args.htmltable)
#remove tab, space and newline then reassigned
htmltable = re.sub(r'\s+', '', htmltable)

tablelist = re.findall(r'\<table.*?/table\>',htmltable)

print(f"Found {len(tablelist)} table in the html")

#loop for table to get row
for table in tablelist:
	tablerow = []
	rowlist = re.findall(r'\<tr.*?/tr\>', table)
	tablerow.append(rowlist)
	
	#loop row to get data
	for tabledata in rowlist:
		datalist = re.findall(r'\<th.*?/th\>|\<td.*?/td\>', tabledata)
	
	print(f"This table contain {len(tablerow[0])} row")
	print(f"Each row contain {len(datalist)} data")
