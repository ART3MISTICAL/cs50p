def main():
    text = input('Input: ')
    shortened = shorten(text)
    print('Output:', shortened)


def isVowel(letter):
    if (letter == 'a' or letter == 'e' or letter == 'i' or
        letter == 'o' or letter == 'u' or letter == 'A' or
        letter == 'E' or letter == 'I' or letter == 'O' or
        letter == 'U'):
        return True
    else:
        return False

def shorten(text):
    shortened = ''
    for letter in text:
        if isVowel(letter):
            pass
        else:
            shortened += letter
    return shortened

if __name__ == "__main__":
    main()