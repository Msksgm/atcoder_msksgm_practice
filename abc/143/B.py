from itertools import combinations


def main():
    n = int(input())
    ds = map(int, input().split())

    ans = 0
    for d in combinations(ds, 2):
        ans += d[0]*d[1]

    print(ans)


if __name__ == "__main__":
    main()
