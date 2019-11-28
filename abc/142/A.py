def main():
    n = int(input())
    odds = 0

    for i in range(1, n+1):
        if i % 2 != 0:
            odds += 1
    print(odds/n)


if __name__ == "__main__":
    main()
