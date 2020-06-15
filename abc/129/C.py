def main():
    n, m = map(int, input().split())
    As = set([int(input()) for _ in range(m)])
    mod = 1000000007

    dp = [0] * (n + 1)
    dp[0] = 1
    if 1 not in As:
        dp[1] = 1

    for i in range(2, n+1):
        if i in As:
            continue
        dp[i] = dp[i-1] + dp[i-2]

    ans = dp[n] % mod
    print(ans)


if __name__ == "__main__":
    main()
