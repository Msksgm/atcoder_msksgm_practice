def main():
    n, k = map(int, input().split())
    ps = list(map(int, input().split()))
    ans = sum(sorted(ps)[:k])
    print(ans)


if __name__ == "__main__":
    main()
