import numpy as np


def main():
    N, L = map(int, input().split())
    Ns = np.array(range(1, N+1)) + L - 1
    abs_Ns = np.where(Ns < 0, Ns*-1, Ns)
    eat_indx = np.where(abs_Ns == np.min(abs_Ns))[0][0]
    ans = np.sum(np.delete(Ns, eat_indx, 0))
    print(ans)


if __name__ == "__main__":
    main()
