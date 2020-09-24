def main():
    n, m = map(int, input().split())
    if n >= 12:
        n -= 12
    n = n * 30 + m * 0.5
    m = m * 6
    if m >= n:
        ans = min(abs(m-n), abs(360-abs(m-n)))
    else:
        ans = min(abs(n-m), abs(360-abs(n-m)))

    print(ans, end="\n")


if __name__ == "__main__":
    main()
