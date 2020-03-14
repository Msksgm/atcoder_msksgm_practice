def cf(x1, x2):
    cf = [1]
    for i in range(2, min(x1, x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf


def main():
    a, b, k = map(int, input().split())
    ab_cf = cf(a, b)
    ans = sorted(ab_cf)[-k]
    print(ans)


if __name__ == "__main__":
    main()
