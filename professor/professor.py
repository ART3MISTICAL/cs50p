import random

levels = [
    1,
    2,
    3
]


def main():
    level = get_level()
    score = round_score(level)

    print('Score:', score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                break

        except:
            pass

    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y

def round(x,y):
    tries = 1
    ans = x + y
    while tries <= 3:
        try:
            get_ans = int(input(f"{x} + {y} = "))
            if get_ans == ans:
                return True
            else:
                tries += 1
                print ('EEE')
        except:
            tries += 1
            print ('EEE')

    print(x,'+',y,'=',ans)
    return False

def round_score(level):
    rounds = 1
    score = 0

    while rounds <= 10:
        x, y = generate_integer(level)
        response = round(x,y)

        if response == True:
            score += 1

        # else:
        #     return score
        rounds += 1

    return score

if __name__ == "__main__":
    main()