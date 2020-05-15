import numpy as np


def main():
    n = int(input())
    As = np.array(list(map(int, input().split())))

    for i in range(n):
        print(np.sum(As == i+1))


if __name__ == "__main__":
    main()
