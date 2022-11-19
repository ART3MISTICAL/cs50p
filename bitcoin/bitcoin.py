import sys
import requests

if len(sys.argv) == 2:
    try:
        number = float(sys.argv[1])
    except:
        print('Command-line arguement is not a number')
        sys.exit(1)


else:
    print('Missing command-line argument')
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    index = r.json()
    bitcoin = index['bpi']['USD']['rate_float']
    price = number * bitcoin
    print(f"${price:,.4f}")
except requests.RequestException:
    sys.exit(1)