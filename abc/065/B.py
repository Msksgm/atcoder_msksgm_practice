def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    x = [0]*n
    i = 0
    ans = 0
    while x[i] == 0:
        ans += 1
        x[i] = 1
        i = As[i] - 1
        if i == 1:
            print(ans)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
