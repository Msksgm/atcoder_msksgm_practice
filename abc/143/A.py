def main():
    n, m = map(int, input().split())
    if n <= m*2:
        print(0)
    else:
        print(n-m*2)


if __name__ == "__main__":
    main()
