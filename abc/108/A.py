from itertools import combinations as comb


def main():
    k = int(input())
    pairs = list(comb(range(1, k+1), 2))

    ans = 0
    for pair in pairs:
        if pair[0] % 2 == 0 and pair[1] % 2 != 0:
            ans += 1
        elif pair[0] % 2 != 0 and pair[1] % 2 == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
