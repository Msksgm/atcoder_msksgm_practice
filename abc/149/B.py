def main():
    a, b, k = map(int, input().split())
    if a == 0 and b == 0:
        print(a, b)
    elif a <= k:
        a_diff = k - a
        a = 0
        if b <= a_diff:
            b = 0
            print(a, b)
        else:
            b -= a_diff
            print(a, b)
    else:
        a = a - k
        print(a, b)


if __name__ == "__main__":
    main()
