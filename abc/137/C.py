def main():
    n = int(input())
    s = ["".join(sorted(input())) for _ in range(n)]
    ans = 0
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] += 1
            ans += dic[i]
        # print(ans)
    print(ans)


if __name__ == "__main__":
    main()
