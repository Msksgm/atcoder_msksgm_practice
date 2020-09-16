import numpy as np


def main():
    n = int(input())
    ss = []
    ps = []
    for _ in range(n):
        s, p = input().split()
        ss.append(s)
        ps.append(int(p))

    popluarity = np.sum(ps)
    ans_index = np.where(np.array(ps) > popluarity//2)[0]
    if len(ans_index) == 0:
        ans = "atcoder"
    else:
        ans = ss[ans_index[0]]
    print(ans)


if __name__ == "__main__":
    main()
