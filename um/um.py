import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    times = len(re.findall(r'\b\W*um\W*', s, re.IGNORECASE))
    return times


if __name__ == "__main__":
    main()