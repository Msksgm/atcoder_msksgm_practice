def main():
    a, b, c, k = map(int, input().split())

    ans = 0
    if k >= a:
        ans += a
        k = k - a
        if k >= b:
            k = k - b
            ans -= k
            print(ans)
        else:
            print(ans)
    else:
        ans += k
        print(ans)


if __name__ == "__main__":
    main()
