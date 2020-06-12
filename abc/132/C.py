def main():
    n = int(input())
    ds = sorted(list(map(int, input().split())))

    if n % 2 != 0:
        ans = 0
    else:
        mid = n // 2
        ans = ds[mid] - ds[mid-1]
    print(ans)


if __name__ == "__main__":
    main()
