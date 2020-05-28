def main():
    n, k = map(int, input().split())
    ps = list(map(int, input().split()))
    e = [(1+p)/2 for p in ps]

    s = [0]
    for i in range(n):
        s.append(s[i]+e[i])

    ans = max([s[i+k] - s[i] for i in range(n-k+1)])
    print(ans)


if __name__ == "__main__":
    main()
