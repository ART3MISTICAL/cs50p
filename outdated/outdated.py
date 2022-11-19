months = {
    "January" : '1',
    "February" : '2',
    "March" : '3',
    "April" : '4',
    "May" : '5',
    "June" : '6',
    "July" : '7',
    "August" : '8',
    "September" : '9',
    "October" : '10',
    "November" : '11',
    "December" : '12'
}
while True:
    get_date = input("Date: ")
    try:
        if '/' in get_date:
            get_date = get_date.replace('/', ' ')
            month, date, year = get_date.split(' ')
            if int(month) < 10:
                month = '0' + month
            if int(date) < 10:
                date = '0' + date
            if int(date) > 31 or int(month) > 12:
                pass
            else:
                print (year,month,date, sep = '-')
                break
        elif ',' in get_date:
            get_date = get_date.replace(',', '')
            month, date, year = get_date.split()
            month_num = months[month]
            if int(month_num) < 10:
                month_num = '0' + month_num
            if int(date) < 10:
                date = '0' + date
            if int(date) > 31 or int(month_num) > 12:
                pass
            else:
                print (year,month_num,date, sep = '-')
                break


    except:
        pass

