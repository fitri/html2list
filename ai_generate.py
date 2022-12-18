# Import the required modules
import html.parser
import re

# Define the HTML parser class
class TableParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.tables = []
        self.current_table = []
        self.current_row = []
        self.current_cell = ""

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tr" and self.in_table:
            self.current_row = []
        elif tag == "td" and self.in_table:
            self.current_cell = ""

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
            self.tables.append(self.current_table)
            self.current_table = []
        elif tag == "tr" and self.in_table:
            self.current_table.append(self.current_row)
        elif tag == "td" and self.in_table:
            self.current_row.append(self.current_cell)

    def handle_data(self, data):
        if self.in_table:
            # Remove all escape characters from the data
            data = re.sub(r"\\", "", data)
            self.current_cell += data

# Open the HTML file and read its contents
with open("simpletable.html", "r") as f:
    html_data = f.read()

# Create a TableParser object and feed it the HTML data
parser = TableParser()
parser.feed(html_data)

# Extract the tables from the parser object and print them
tables = parser.tables
for table in tables:
    print(table)
