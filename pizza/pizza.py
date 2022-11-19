import sys
import csv
from tabulate import tabulate

table = [

]

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

elif '.csv' not in sys.argv[1]:
    sys.exit('Not a CSV file')

try:
    f = open(sys.argv[1])
    reader = csv.reader(f)
    for row in reader:
        table.append(row)
    # print(table)
    print(tabulate(table[1:], headers = table[0], tablefmt = 'grid'))
    f.close()
except FileNotFoundError:
    sys.exit('File does not exist')
