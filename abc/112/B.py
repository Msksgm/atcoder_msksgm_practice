def main():
    n, T = map(int, input().split())
    cts = [list(map(int, input().split())) for _ in range(n)]
    ans = float("inf")
    for ct in cts:
        c, t = ct
        if t <= T:
            ans = min(ans, c)

    if ans == float("inf"):
        ans = "TLE"

    print(ans)


if __name__ == "__main__":
    main()
