def main():
    n = int(input())
    ps = [int(input()) for _ in range(n)]
    ps.sort(reverse=True)
    ans = ps[0]//2 + sum(ps[1:])
    print(ans)


if __name__ == "__main__":
    main()
