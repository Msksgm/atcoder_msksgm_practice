def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ans = 0
    minp = float("inf")
    for p in ps:
        minp = min(minp, p)
        if minp >= p:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
