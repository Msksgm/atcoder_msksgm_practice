import sys


def main():
    ss = input()
    ts = input()
    n = len(ss)

    for i in range(n):
        ss = ss[-1] + ss[:-1]
        if ss == ts:
            print('Yes')
            sys.exit(0)

    print("No")


if __name__ == "__main__":
    main()
