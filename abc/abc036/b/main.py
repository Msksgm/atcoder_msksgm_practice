def main():
    n = int(input())
    ans = [['' for i in range(n)] for j in range(n)]
    sss = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] += sss[-1-j][i]
    
    for i in range(n):
        print(*ans[i], sep='')


if __name__ == "__main__":
    main()
