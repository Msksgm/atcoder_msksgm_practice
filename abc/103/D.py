def main():
    n, m = map(int, input().split())
    # ab = [list(map(int, input().split())) for _ in range(m)]
    ab = [[]*2]*m
    for i in range(m):
        ab[i] = list(map(int, input().split()))
    # print(ab)
    ab.sort
    count = 0
    r = ab[0][1] - 1
    count += 1
    for i in range(1, m):
        if ab[i][1] - 1 < r:
            r = ab[i][1] - 1
        if r < ab[i][0]:
            r = ab[i][1] - 1
            count += 1
    print(count)


if __name__ == "__main__":
    main()
