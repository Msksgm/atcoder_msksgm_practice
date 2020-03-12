import numpy as np
from itertools import combinations as comb


def main():
    n, d = map(int, input().split())
    xs = [list(map(int, input().split())) for _ in range(n)]
    xs_combs = list(comb(xs, 2))
    ans = 0
    for xs_comb in xs_combs:
        xs_comb = np.array(xs_comb)
        dist = np.linalg.norm(xs_comb[0]-xs_comb[1])
        if int(dist) == dist:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
