def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    m = int(input())
    ts = [input() for _ in range(m)]

    fruits = list(set(ss))
    ans = 0
    for fruit in fruits:
        money = 0
        money += ss.count(fruit)
        money -= ts.count(fruit)
        ans = max(ans, money)
    print(ans)


if __name__ == "__main__":
    main()
