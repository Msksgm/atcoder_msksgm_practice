import sys


def main():
    s = list(input())
    if s[0] != 'A' or s[2:-1].count("C") != 1:
        print("WA")
    else:
        for i in range(1, len(s)):
            if ord(s[i]) < ord('a') and i != s.index('C'):
                print("WA")
                sys.exit(0)
        print("AC")


if __name__ == "__main__":
    main()
