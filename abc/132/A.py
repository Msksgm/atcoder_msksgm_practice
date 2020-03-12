import sys


def main():
    s = list(input())
    set_s = set(s)
    if len(set_s) != 2:
        print("No")
        sys.exit(0)
    for x in set_s:
        if s.count(x) != 2:
            print("No")
            sys.exit(0)
    print("Yes")


if __name__ == "__main__":
    main()
