def main():
    n = int(input())
    xus = [input() for _ in range(n)]
    ans = 0
    for xu in xus:
        x, u = xu.split()
        if u == "JPY":
            ans += float(x)
        if u == "BTC":
            ans += float(x) * 380000.0

    print(ans)


if __name__ == "__main__":
    main()
