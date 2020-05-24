def main():
    n, m = map(int, input().split())
    ans = [0]*n
    for _ in range(m):
        s, c = map(int, input().split())
        if ans[s-1] == 0:
            ans[s-1] = c
        elif ans[s-1] != 0 and ans[s-1] != c:
            print(-1)
            exit()

    if ans[0] == 0:
        print(-1)
    else:
        print(*ans, sep="")


if __name__ == "__main__":
    main()
