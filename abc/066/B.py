def main():
    s = input()
    for i in range(1, len(s)):
        r = s[:-i]
        q = len(s[:-i])
        if q % 2 != 0:
            continue
        if r[:q//2] == r[q//2:]:
            ans = q
            break
    print(ans)


if __name__ == "__main__":
    main()
