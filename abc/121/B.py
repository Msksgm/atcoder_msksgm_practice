import numpy as np


def main():
    n, m, c = map(int, input().split())
    B = list(map(int, input().split()))
    As = [list(map(int, input().split())) for _ in range(n)]

    B_arr = np.array(B)
    ans = 0
    for A in As:
        A_arr = np.array(A)
        judge = np.sum((B_arr*A_arr)) + c
        if judge > 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
