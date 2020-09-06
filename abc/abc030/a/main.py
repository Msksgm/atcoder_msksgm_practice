def main():
    a, b, c, d = map(int, input().split())
    taka = (b/a)
    ao = (d/c)
    if taka == ao:
        ans = "DRAW"
    elif taka > ao:
        ans = "TAKAHASHI"
    else:
        ans = "AOKI"
    print(ans)


if __name__ == "__main__":
    main()
