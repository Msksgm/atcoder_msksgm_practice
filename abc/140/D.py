def main():
    n, k = map(int, input().split())
    s = input()
    a = s.count("RL")  # RLの順に並んでいる箇所をカウント
    ans = 0  # 答えを初期化
    # print("a=", a)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ans += 1  # 最初の点数をカウント
    for i in range(1, k + 1):
        # print("i=", i)
        # print("ans=", ans)
        # print("n-1-ans=", n - 1 - ans)
        if n - 1 - ans > 1:
            ans += 2
        else:
            ans += n - 1 - ans
            break
    print(ans)


if __name__ == "__main__":
    main()
