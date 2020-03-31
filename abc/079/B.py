def main():
    n = int(input())
    lucas = [0 for _ in range(n+1)]

    for i in range(n+1):
        if i == 0:
            lucas[i] = 2
        elif i == 1:
            lucas[i] = 1
        else:
            lucas[i] = lucas[i-1] + lucas[i-2]

    ans = lucas[-1]
    print(ans)


if __name__ == "__main__":
    main()
