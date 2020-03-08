import numpy as np


def main():
    As = [list(map(int, input().split())) for j in range(3)]
    As = np.array(As)
    n = int(input())
    bs = [int(input()) for i in range(n)]
    for b in bs:
        As = np.where(As == b, 0, As)

    if np.any(np.all(As == 0, axis=0)):
        print("Yes")
    elif np.any(np.all(As == 0, axis=1)):
        print("Yes")
    elif As[0][0] == 0 and As[1][1] == 0 and As[2][2] == 0:
        print("Yes")
    elif As[0][2] == 0 and As[1][1] == 0 and As[2][0] == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
