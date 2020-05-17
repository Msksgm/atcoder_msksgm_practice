def main():
    n, k = map(int, input().split())

    if n % k == 0:
        ans = 0
    else:
        ans_temp = n % k
        ans = min(ans_temp, abs(ans_temp - k))

    print(ans)


if __name__ == "__main__":
    main()
