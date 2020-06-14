def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        temp = i
        j = 0
        while temp < k:
            temp *= 2
            j += 1
        ans += (1/2)**j
    print(ans/n)


if __name__ == "__main__":
    main()
