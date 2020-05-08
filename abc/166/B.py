def main():
    n, k = map(int, input().split())
    s = []
    ans_temp = [i for i in range(1, n+1)]
    for _ in range(k):
        d = int(input())
        As = map(int, input().split())
        s.extend(As)
    ans = len(set(ans_temp)) - len(set(s))
    print(ans)


if __name__ == "__main__":
    main()
