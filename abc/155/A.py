from itertools import combinations as comb


def main():
    a, b, c = map(int, input().split())
    li = comb([a, b, c], 2)
    Count = 0
    for l in li:
        if l[0] == l[1]:
            Count += 1

    if Count == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
