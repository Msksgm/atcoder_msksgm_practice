def main():
    n = int(input())
    s = list(input())

    x = 0
    ans = 0
    for i in range(n):
        if s[i] == 'I':
            x += 1
        if s[i] == 'D':
            x -= 1
        ans = max(ans, x)
    print(ans)


if __name__ == "__main__":
    main()
