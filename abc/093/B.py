def main():
    a, b, k = map(int, input().split())
    s = set()

    for i in range(a, min(a+k, b+1)):
        s.add(i)

    for i in range(b, max(a-1, b-k), -1):
        s.add(i)

    s = sorted(s)

    for i in s:
        print(i)


if __name__ == "__main__":
    main()
