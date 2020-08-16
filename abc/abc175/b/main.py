from collections import Counter
from itertools import combinations as comb


def main():
    n = int(input())
    ls = list(map(int, input().split()))
    ls_count = Counter(ls)
    ls_keys = list(ls_count.keys())
    m = len(ls_keys)
    ans = 0
    for i in range(m-2):
        c = ls_keys[i]
        pairs = list(comb(ls_keys[(i+1):], 2))
        for a, b in pairs:
            if c + a > b and a + b > c and b + c > a:
                ans += ls_count[c] * ls_count[a] * ls_count[b]
    print(ans)


if __name__ == "__main__":
    main()
