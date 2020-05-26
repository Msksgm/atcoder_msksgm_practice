def main():
    n, k = map(int, input().split())
    hs = list(map(int, input().split()))

    hs = sorted(hs)[::-1]
    ans = sum(hs[k:])
    print(ans)


if __name__ == "__main__":
    main()
