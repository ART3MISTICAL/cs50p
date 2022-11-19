import sys
import csv

output = [

]

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
    sys.exit('Not a CSV file')

try:
    f = open(sys.argv[1])
    reader = csv.DictReader(f)
    for row in reader:
        names = row['name'].split(',')
        output.append({'first': names[1].lstrip(),
                      'last': names[0], 'house': row['house']})
    f.close()

except FileNotFoundError:
    sys.exit('Could not read', sys.argv[1])

f2 = open(sys.argv[2], 'w')
writer = csv.DictWriter(f2, fieldnames = ['first', 'last', 'house'])
writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
for row in output:
    writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

f2.close()