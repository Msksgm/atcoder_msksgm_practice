def main():
    n = int(input())
    t, a = map(int, input().split())
    hs = list(map(int, input().split()))
    diff = float("inf")
    for i in range(n):
        temp = t - hs[i] * 0.006
        if diff > abs(temp - a):
            diff = abs(temp - a)
            ans = i + 1
    print(ans)


if __name__ == "__main__":
    main()
