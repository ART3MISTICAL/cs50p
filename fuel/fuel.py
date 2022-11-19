def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    output = gauge(int(percentage))
    print(output)

def convert(fraction):
    while True:
        try:
            num, den = fraction.split('/')
            num = int(num)
            den = int(den)
            fraction = num/den
            if fraction > 1:
                fraction = 'error'
            fuel = str(int(fraction*100))+'%'
            return fraction*100
        except (ValueError, ZeroDivisionError):
            pass



def gauge(percentage):

    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return str(percentage) + '%'


if __name__ == "__main__":
    main()