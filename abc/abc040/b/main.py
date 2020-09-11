def main():
    n = int(input())
    ans = float("inf")
    for h in range(1, n+1):
        w = n // h
        ans = min(ans, abs(h-w)+n-h*w)
    print(ans)


if __name__ == "__main__":
    main()
