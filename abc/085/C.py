def main():
    n, y = map(int, input().split())
    for i in range(n+1):
        for j in range(n-i+1):
            k = (n-i-j)
            if (i * 10000 + j * 5000 + k * 1000) == y:
                ans = [i, j, k]
                print(*ans)
                exit()
    ans = [-1, -1, -1]
    print(*ans)


if __name__ == "__main__":
    main()
