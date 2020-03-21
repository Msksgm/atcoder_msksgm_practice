def main():
    n, x = map(int, input().split())
    ms = [int(input()) for _ in range(n)]

    x = x - sum(ms)
    min_m = min(ms)
    i = 0
    while True:
        x = x - min_m
        if x < 0:
            break
        i += 1
    ans = n + i
    print(ans)


if __name__ == "__main__":
    main()
