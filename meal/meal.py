def main():
    get_time = input('What time is it? ')

    time = convert(get_time)

    if time >= 7 and time <= 8:
        print('breakfast time')

    elif time >= 12 and time <= 13:
        print('lunch time')

    elif time >= 18 and time <= 19:
        print ('dinner time')

def convert(time):
    if 'p.m.' in time:
        new_time = time.replace('p.m.', '')
        hour, minute = new_time.split(':')
        converted_time = float(hour) + (float(minute)/60) + 12
    elif 'a.m.' in time:
        new_time = time.replace('a.m.', '')
        hour, minute = new_time.split(':')
        converted_time = float(hour) + (float(minute)/60)
    else:
        hour, minute = time.split(':')
        converted_time = float(hour) + (float(minute)/60)
    return converted_time

if __name__ == "__main__":
    main()