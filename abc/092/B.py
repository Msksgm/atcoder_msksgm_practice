def main():
    n = int(input())
    d, x = map(int, input().split())
    As = [int(input()) for _ in range(n)]

    ans = 0
    for a in As:
        i = 0
        while True:
            if i*a+1 > d:
                break
            ans += 1
            i += 1
    ans += x
    print(ans)


if __name__ == "__main__":
    main()
