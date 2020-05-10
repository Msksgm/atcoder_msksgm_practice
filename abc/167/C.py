import numpy as np


def main():
    n, m, x = map(int, input().split())
    cas = np.array([list(map(int, input().split())) for _ in range(n)])

    ans = -1
    for i in range(2 ** n):
        if i == 0:
            continue
        books = []
        for j in range(n):
            if ((i >> j) & 1):
                books.append(cas[j])

        books = np.array(books)
        if np.all(np.sum(books[:, 1:], axis=0) >= x):
            ans_temp = np.sum(books[:, 0])
            if ans == -1:
                ans = ans_temp
            else:
                ans = min(ans, ans_temp)
    print(ans)


if __name__ == "__main__":
    main()
