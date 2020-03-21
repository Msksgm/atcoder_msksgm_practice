def main():
    x = int(input())
    ans = 1
    for b in range(x, 1, -1):
        p = 2
        ans_temp = -float("inf")
        while True:
            if b**p > x:
                break
            ans_temp = b**p
            p += 1
        ans = max(ans, ans_temp)
    print(ans)


if __name__ == "__main__":
    main()
