def main():
    n = int(input())
    As = sorted(list(map(int, input().split())))

    a = As[0]
    b = As[-1]

    ans = b - a
    print(ans)


if __name__ == "__main__":
    main()
