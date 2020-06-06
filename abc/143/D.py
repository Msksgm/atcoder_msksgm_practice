import bisect


def main():
    n = int(input())
    ls = sorted(list(map(int, input().split())))

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a = ls[i]
            b = ls[j]
            k = bisect.bisect_left(ls, a+b)
            if k > j:
                ans += k - j - 1
    print(ans)


if __name__ == "__main__":
    main()
