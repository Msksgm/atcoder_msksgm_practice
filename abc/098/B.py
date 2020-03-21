def main():
    n = int(input())
    s = input()

    ans = -float("inf")
    for i in range(1, n):
        s_union = set(s[:i]) & set(s[i:])
        ans = max(ans, len(s_union))
    print(ans)


if __name__ == "__main__":
    main()
