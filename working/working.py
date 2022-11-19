def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        start, ampm, to, end, pmam = s.split()
        if to != 'to':
            raise ValueError
        if ':' in s:
            hr, mi = start.split(':')
            hr2, mi2 = end.split(':')
            if int(mi) >= 60:
                raise ValueError
            if int(mi2) >= 60:
                raise ValueError
            if ampm == 'AM':
                hrs, mins = start.split(':')
                if hrs == '12':
                    startx = (f'00:{mins}')
                elif int(hrs) < 10:
                    startx = (f'0{start}')
                else:
                    startx = start
            if ampm == 'PM':
                hrs, mins = start.split(':')
                if hrs == '12':
                    startx = (f'12:{mins}')
                else:
                    hrs = int(hrs) + 12
                    startx = (f'{hrs}:{mins}')

            if pmam == 'AM':
                hre, mine = end.split(':')
                if hre == '12':
                    endx = (f'00:{mine}')
                elif int(hre) < 10:
                    endx = (f'0{end}')
                else:
                    endx = end

            if pmam == 'PM':
                hre, mine = end.split(':')
                if hre == '12':
                    endx = (f'12:{mine}')
                else:
                    hre = int(hre) + 12
                    endx = (f'{hre}:{mine}')
            return (f'{startx} {to} {endx}')

        else:
            if ampm == 'AM':
                if int(start) == 12:
                    startx = '00:00'
                elif int(start) < 10:
                    startx = (f'0{start}:00')
                else:
                    startx = (f"{start}:00")

            if ampm == 'PM':
                if start == '12':
                    startx = '12:00'
                else:
                    start = int(start) + 12
                    startx = (f'{start}:00')

            if pmam == 'AM':
                if int(end) < 10:
                    endx = (f'0{end}:00')
                else:
                    endx = (f'{end}:00')

            if pmam == 'PM':
                if int(end) == 12:
                    endx = '12:00'
                else:
                    end = int(end) + 12
                    endx = (f'{end}:00')
            return (f'{startx} {to} {endx}')

    except:
        raise ValueError



if __name__ == "__main__":
    main()