def main():
    n, q = map(int, input().split())
    anss = [0 for _ in range(n)]
    for i in range(q):
        l, r, t = map(int, input().split())
        for i in range(l-1, r):
            anss[i] = t

    for ans in anss:
        print(ans)


if __name__ == "__main__":
    main()
