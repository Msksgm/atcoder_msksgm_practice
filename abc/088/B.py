def main():
    n = int(input())
    As = sorted(list(map(int, input().split())))[::-1]

    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += As[i]
        else:
            bob += As[i]

    ans = alice - bob
    print(ans)


if __name__ == "__main__":
    main()
