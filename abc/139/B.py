import math


def main():
    a, b = map(int, input().split())

    ans = 1
    c = 0
    while ans < b:
        ans += a - 1
        c += 1

    print(c)


if __name__ == "__main__":
    main()
