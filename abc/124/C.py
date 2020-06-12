def main():
    ss = list(input())
    n = len(ss)

    ans1 = 0
    ans2 = 0
    for i in range(n):
        if i % 2 == 0 and ss[i] == "1":
            ans1 += 1
        if i % 2 != 0 and ss[i] == "0":
            ans1 += 1

    for i in range(n):
        if i % 2 == 0 and ss[i] == "0":
            ans2 += 1
        if i % 2 != 0 and ss[i] == "1":
            ans2 += 1
    ans = min(ans1, ans2)
    print(ans)


if __name__ == "__main__":
    main()
