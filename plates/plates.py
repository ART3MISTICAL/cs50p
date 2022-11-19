def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >=2 and s[0:2].isalpha() and s.isalnum():

        for n in range(len(s)):
            if s[n].isdigit():
                if not s[n:].isdigit():
                    return False
        for i in s:
            if i.isdigit():
                if i != '0':
                    return True

                if i == '0':
                    return False

            else:
                pass


        if s.isalpha():
            return True



    else:
        return False



if __name__ == "__main__":
    main()