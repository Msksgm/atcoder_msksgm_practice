def main():
    n = int(input())
    ws = list(map(int, input().split()))

    ans = float("inf")
    for i in range(1, n):
        left = sum(ws[:i])
        right = sum(ws[i:])
        diff = abs(left - right)
        ans = min(ans, abs(diff))
    print(ans)


if __name__ == "__main__":
    main()
