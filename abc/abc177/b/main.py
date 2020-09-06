def main():
    ss = list(input())
    ts = list(input())
    n, m = len(ss), len(ts)
    ans = float("inf")
    for i in range(n-m+1):
        ans_temp = 0
        for j in range(m):
            if ss[i+j] != ts[j]:
                ans_temp += 1
        ans = min(ans, ans_temp)
    print(ans)


if __name__ == "__main__":
    main()
