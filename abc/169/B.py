def main():
    n = int(input())
    As = list(map(int, input().split()))

    ans = 1
    if 0 in As:
        print(0)
        exit()

    for i in range(n):
        ans *= As[i]
        if ans > 10**18:
            ans = -1
            break

    print(ans)


if __name__ == "__main__":
    main()
