def main():
    n = int(input())
    s = list(input())

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if j-i == k-j:
                    continue
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
