def main():
    s = list(input())

    n = len(s)
    start = -1
    for i in range(n):
        if s[i] == 'A' and start == -1:
            start = i
        if s[i] == 'Z':
            end = i

    ans = end - start + 1
    print(ans)


if __name__ == "__main__":
    main()
