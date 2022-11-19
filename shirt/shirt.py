import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

elif '.png' not in sys.argv[1] and '.jpg' not in sys.argv[2]:
    sys.exit('Input and output have different extensions')

elif '.jpg' not in sys.argv[1] and '.png' not in sys.argv[2]:
    sys.exit('Input and output have different extensions')

elif '.jpg' not in sys.argv[1] or '.jpg' not in sys.argv[2]:
    sys.exit('Invalid output')

try:
    f = Image.open(sys.argv[1])

except FileNotFoundError:
    sys.exit('Input does not exist')

shirt = Image.open('shirt.png')
size = shirt.size
f = ImageOps.fit(f, size)
f.paste(shirt, shirt)
f.save(sys.argv[2])