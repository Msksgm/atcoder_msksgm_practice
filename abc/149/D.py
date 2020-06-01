def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    ts = list(input())

    hands = {"r": p, "s": r, "p": s}
    ans = 0
    skip = [0]*n
    for i in range(n):
        if skip[i] == 1:
            continue

        if i+k > n-1:
            ans += hands[ts[i]]

        else:
            if ts[i] != ts[i+k]:
                ans += hands[ts[i]]
            else:
                ans += hands[ts[i]]
                skip[i+k] = 1

    print(ans)


if __name__ == "__main__":
    main()
