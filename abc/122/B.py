def main():
    s = list(input())
    n = len(s)
    acgt = ["A", "C", "G", "T"]
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            flag = True
            for k in s[i:j]:
                if k not in acgt:
                    flag = False
                    break
            if flag:
                ans = max(len(s[i:j]), ans)
    print(ans)


if __name__ == "__main__":
    main()
