def main():
    n = int(input())
    As = list(map(int, input().split()))

    std = As[0]
    ans = 0
    for i in range(1, n):
        if std >= As[i]:
            ans += std - As[i]
        else:
            std = As[i]
    print(ans)


if __name__ == "__main__":
    main()
