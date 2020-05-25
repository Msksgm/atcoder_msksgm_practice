def main():
    n = int(input())
    xs = list(map(int, input().split()))
    x_min = min(xs)
    x_max = max(xs)

    ans = float("inf")
    for i in range(x_min, x_max+1):
        ans_temp = 0
        for x in xs:
            ans_temp += (x - i)**2
        ans = min(ans, ans_temp)

    print(ans)


if __name__ == "__main__":
    main()
