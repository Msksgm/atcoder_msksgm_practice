def main():
    n = int(input())
    ts = [int(input()) for _ in range(n)]
    thresh = float("inf")
    for i in range(n**2):
        right = []
        left = []
        for j in range(n):
            if (i >> j) & 1:
                right.append(ts[j])
            else:
                left.append(ts[j])
        # if abs(sum(right)-sum(left)) < thresh:
        # print(right, left)
        if thresh > abs(sum(right)-sum(left)):
            thresh = min(thresh, abs(sum(right)-sum(left)))
            ans = max(sum(right), sum(left))
        # print(thresh)
    print(ans)


if __name__ == "__main__":
    main()
