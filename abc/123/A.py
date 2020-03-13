from itertools import combinations as comb
import sys


def main():
    antennas = [int(input()) for _ in range(5)]
    k = int(input())

    pair_antenna = list(comb(antennas, 2))
    for pair in pair_antenna:
        diff = pair[1] - pair[0]
        if diff > k:
            print(":(")
            sys.exit(0)
    print("Yay!")


if __name__ == "__main__":
    main()
