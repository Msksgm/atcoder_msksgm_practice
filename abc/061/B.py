def main():
    n, m = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(m)]
    anss = [0]*n
    for AB in ABs:
        anss[AB[0]-1] += 1
        anss[AB[1]-1] += 1
    for ans in anss:
        print(ans)


if __name__ == "__main__":
    main()
