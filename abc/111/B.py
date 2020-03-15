import sys


def main():
    anss = [111, 222, 333, 444, 555, 666, 777, 888, 999]
    n = int(input())
    for ans in anss:
        if ans >= n:
            print(ans)
            sys.exit(0)


if __name__ == "__main__":
    main()
