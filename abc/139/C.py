def main():
    n = int(input())
    h = list(map(int, input().split()))

    if n == 1:
        print(0)
        quit()

    start = 0
    ans = []
    for i in range(n-1):
        if h[i] >= h[i+1]:
            continue
        ans.append(i - start)
        start = i+1

    if h[n-2] >= h[n-1]:
        ans.append(n - 1 - start)

    print(max(ans))


if __name__ == "__main__":
    main()
