from itertools import combinations as comb
import numpy as np


def main():
    p, q, r = map(int, input().split())
    abc_comb = np.array(list(comb([p, q, r], 2)))
    print(np.min(np.sum(abc_comb, axis=1)))


if __name__ == "__main__":
    main()
