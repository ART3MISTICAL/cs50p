import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            number = random.randint(1, level)
            break
        else:
            pass
    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > number:
                print('Too large!')
                pass
            elif guess < number:
                print('Too small!')
                pass
            else:
                print('Just right!')
                break
        else:
            pass
    except ValueError:
        pass