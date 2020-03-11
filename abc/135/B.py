def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ps_sort = sorted(ps)

    Count = 0
    for i, j in zip(ps, ps_sort):
        if i != j:
            Count += 1

    if Count == 2 or Count == 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
