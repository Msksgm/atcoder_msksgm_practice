import sys


def main():
    n, a, b = map(int, input().split())

    if a == 0:
        print(0)
        sys.exit(0)
    if b == 0:
        ans = n
        print(ans)
        sys.exit(0)
    div = n // (a+b)
    mod = n % (a+b)
    ans = div * a
    if a >= mod:
        ans += mod
    else:
        ans += a
    print(ans)


if __name__ == "__main__":
    main()
