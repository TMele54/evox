import csv
with open('C:\\Users\\tonym\\OneDrive\\AAM_Portfolio\\evox\\data\\regexes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        pass#print(row[2])

str = "the is a stinr gof information and so eo we do wha 185.64.34.543"


pat = "\d[^ ]*+"

import re
p = re.compile("\d{0,}\.\d{0,}\.\d{0,}\.\d{0,}")

print p.findall(str)
