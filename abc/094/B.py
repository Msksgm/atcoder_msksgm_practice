def main():
    n, m, x = map(int, input().split())
    As = list(map(int, input().split()))

    line = [0 for _ in range(n+1)]
    for i in range(n+1):
        if i in As:
            line[i] += 1
    ans = min(sum(line[:x]), sum(line[x:]))
    print(ans)


if __name__ == "__main__":
    main()
