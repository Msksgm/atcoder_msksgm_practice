import sys


def main():
    n = int(input())
    ws = [input() for _ in range(n)]

    for i in range(n-1):
        if ws.count(ws[i]) > 1:
            print('No')
            sys.exit(0)

        if ws[i][-1] != ws[i+1][0]:
            print('No')
            sys.exit(0)

    print('Yes')


if __name__ == "__main__":
    main()
