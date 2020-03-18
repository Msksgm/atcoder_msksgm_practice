import sys


def main():
    n = int(input())
    a = n // 7
    for i in range(a+1):
        mod = n - i*7
        if mod % 4 == 0:
            print('Yes')
            sys.exit(0)
    print('No')


if __name__ == "__main__":
    main()
