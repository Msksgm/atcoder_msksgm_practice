def main():
    a, b, k = map(int, input().split())
    if a <= k:
        a_diff = k - a
        a = 0
        b -= a_diff
        print(a, b)
    else:
        a = a - k
        print(a, b)


if __name__ == "__main__":
    main()
