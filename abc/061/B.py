from collections import Counter


def main():
    n, m = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(m)]
    ABs = [b for a in ABs for b in a]
    anss = Counter(ABs)
    for ans in anss.values():
        print(ans)


if __name__ == "__main__":
    main()
