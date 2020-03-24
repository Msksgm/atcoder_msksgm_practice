def main():
    n = int(input())
    ds = [int(input()) for _ in range(n)]

    ds = set(ds)
    ans = len(ds)
    print(ans)


if __name__ == "__main__":
    main()
