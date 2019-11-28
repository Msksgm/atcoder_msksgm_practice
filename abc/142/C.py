def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    a = {i: k for i, k in enumerate(a, start=1)}
    a = sorted(a.items(), key=lambda a: a[1])
    for i in a:
        ans.append(i[0])

    print(*ans)


if __name__ == "__main__":
    main()
