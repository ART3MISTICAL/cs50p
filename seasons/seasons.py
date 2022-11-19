from datetime import date
import sys
import inflect

e = inflect.engine()

def main():
	print(convert(input('Date of birth: ')))


def convert(m):
	try:
		year, month, day = m.split('-')
		datenow = date.today()
		datex = date(int(year), int(month), int(day))
		# print (datex)
		diff = datenow - datex
		# print (diff)
		diff_in_mins = e.number_to_words(int(diff.total_seconds() /60), andword='')
		return (f'{diff_in_mins.capitalize()} minutes')

	except:
		sys.exit('Invalid date')


if __name__ == "__main__":
	main()