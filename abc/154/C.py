def main():
    n = input()
    As = list(map(int, input().split()))

    if len(As) == len(set(As)):
        ans = "YES"
    else:
        ans = "NO"
    print(ans)


if __name__ == "__main__":
    main()
