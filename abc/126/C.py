def main():
    N, K = map(int, [int(x) for x in input().split()])
    # N, K = map(int,  input().split())
    ans = 0
    for n in range(1, N+1):
        num = n
        i = 0

        while num < K:
            num *= 2
            # n *= 2
            i += 1

        # ans += 1/N*(0.5)**i
        ans += ((1/2)**i)/N

    print(ans)


if __name__ == "__main__":
    main()