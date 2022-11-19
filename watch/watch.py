import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        try:
            f = re.search ("(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)
            f1 = f.groups ()
            return "https://youtu.be/" + f1[3]
        except:
            pass
    else:
        pass

if __name__ == "__main__":
    main()