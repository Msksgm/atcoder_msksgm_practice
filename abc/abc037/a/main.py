def main():
    a, b, c = map(int, input().split())
    min_price = min(a, b)
    max_price = max(a, b)
    ans = (c // min_price)
    ans += (c % min_price) // max_price
    print(ans)


if __name__ == "__main__":
    main()
