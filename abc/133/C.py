def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def main():
    l, r = map(int, input().split())
    ans = float("inf")
    if r - l >= 2500:
        ans = 0
    else:
        for i in range(l, r):
            for j in range(i+1, r+1):
                ans = min((i*j % 2019), ans)
    print(ans)


if __name__ == "__main__":
    main()
