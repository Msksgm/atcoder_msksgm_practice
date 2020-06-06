def main():
    n = int(input())
    ss = list(input())

    ans = 1
    for i in range(1, n):
        if ss[i] == ss[i-1]:
            continue
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
