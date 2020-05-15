def main():
    n = int(input())
    As = list(map(int, input().split()))

    for i in range(n):
        ans = As.count(i+1)
        print(ans)


if __name__ == "__main__":
    main()
