#!/usr/bin/python

import re
import argparse
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("--htmltable", required=True)

args = parser.parse_args()


def gettable(tablepath):
    with open(tablepath) as table:
        return table.read()


# call function with passed arg
htmltable = gettable(args.htmltable)
# remove tab, space and newline then reassigned
htmltable = re.sub(r"\s+", "", htmltable)

tablelist = re.findall(r"\<table.*?/table\>", htmltable)

print(f"Found {len(tablelist)} table in the html")

# loop for table to get row
for tindex, table in enumerate(tablelist):
    # loop table to get list of row
    rowlist = re.findall(
        r"\<tr.*?/tr\>", table
    )  # return list of <tr> tag from <table> tag

    # loop row to get list of data
    for rindex, tabledata in enumerate(rowlist):
        datalist = re.findall(
            r"\<th.*?/th\>|\<td.*?/td\>", tabledata
        )  # return list of <td> from <tr> tag
        rowlist[rindex] = datalist

        # replace the raw table with complete parsed table
    tablelist[tindex] = rowlist
    pprint(tablelist[0][0][0])

# next need to figure out how to append data into row, then row into table to produce single multidimensional list.
