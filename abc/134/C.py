def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    As_sort = sorted(As)
    second, first = As_sort[-2:]
    for i in range(n):
        if As[i] == first:
            print(second)
        else:
            print(first)


if __name__ == "__main__":
    main()
