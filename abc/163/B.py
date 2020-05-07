def main():
    n, m = map(int, input().split())
    As = list(map(int, input().split()))
    if n >= sum(As):
        ans = n - sum(As)
    else:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
