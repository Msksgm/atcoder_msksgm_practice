def main():
    d, n = map(int, input().split())
    div = 100**d
    if n != 100:
        ans = div*n
    else:
        ans = div*n + div

    print(ans)


if __name__ == "__main__":
    main()
