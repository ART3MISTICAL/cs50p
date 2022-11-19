import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    randomFont = True

elif len(sys.argv) ==  3  and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    randomFont = False

else:
    sys.exit(1)

# print (randomFont)



figlet.getFonts()

if randomFont == False:
    try:
        figlet.setFont(font = sys.argv[2])
        text = input('Input: ')
        print ('Output:', figlet.renderText(text), sep = '\n')
    except:
        print('Error')
        sys.exit(1)

else:
    text = input('Input: ')
    font = random.choice(figlet.getFonts())
    print('Output:', figlet.renderText(text), sep = '\n')