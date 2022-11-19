def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        n1, n2, n3, n4 = ip.split('.')
        if int(n1) not in range(0,256):
            return False
        elif int(n2) not in range(0,256):
            return False
        elif int(n3) not in range(0,256):
            return False
        elif int(n4) not in range(0,256):
            return False
        else:
            return True
    except:
        return False



if __name__ == "__main__":
    main()