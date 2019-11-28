import itertools
import numpy as np


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = -1
    for i in list(itertools.combinations(xy, 2)):
        a = np.array(i[0])-np.array(i[1])
        ans = max(ans, np.sqrt(a[0]**2 + a[1]**2))
    print(ans)


if __name__ == "__main__":
    main()
