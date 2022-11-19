import sys

total_lines = 0

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

elif '.py' not in sys.argv[1]:
    sys.exit('Not a Python file')

try:
    f = open(sys.argv[1])
    lines = f.readlines()
    for line in lines:
        if line.isspace():
            pass
        elif line.lstrip().startswith('#'):
            pass
        else:
            total_lines += 1
    print (total_lines)
except FileNotFoundError :
    sys.exit('File does not exist')
