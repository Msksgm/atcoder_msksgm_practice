def main():
    n, a, b = map(int, input().split())

    ans = 0
    for i in range(n+1):
        i = str(i)
        i_str = i
        i = sum(list(map(int, list(i))))
        if a <= i and i <= b:
            ans += int(i_str)
    print(ans)


if __name__ == "__main__":
    main()
