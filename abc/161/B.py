import sys


def main():
    n, m = map(int, input().split())
    As = sorted(list(map(int, input().split())))[::-1]

    all_vote = sum(As)
    for i in range(m):
        if all_vote/(4*m) > As[i]:
            print('No')
            sys.exit()

    print('Yes')


if __name__ == "__main__":
    main()
