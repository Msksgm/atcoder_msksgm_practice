def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        for j in range(1, n):
            c = n - i * j
            if c <= 0:
                break
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
