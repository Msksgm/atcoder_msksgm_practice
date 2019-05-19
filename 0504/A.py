import numpy as np


def main():
    # H, W = [int(x) for x in input().split()]
    H, W = map(int, [int(x) for x in input().split()])
    board = [[0 for i in range(H)] for j in range(W)]

    """ #は1, .は0 """
    for i in range(H):
        X = input()
        X_len = len(X)
        for j in range(X_len):
            if X[j] == "#":
                board[i][j] = 1

    num_board = np.array(board)
    height, width = num_board.shape[:2]
    count = 0
    while (np.sum(num_board) != height*width):
        num_board_ans = np.zeros((height, width))
        for i in range(height):
            if np.sum(num_board[:, j]) == width:
                continue
            for j in range(width):
                if num_board[i, j] == 1:
                    num_board_ans[i, j] = 1
                    a = max(i-1, 0)
                    num_board_ans[a, j] = 1
                    b = max(j-1, 0)
                    num_board_ans[i, b] = 1
                    c = min(i+1, height-1)
                    num_board_ans[c, j] = 1
                    d = min(j+1, width-1)
                    num_board_ans[i, d] = 1
        num_board = num_board_ans
        count += 1

    print(count)


if __name__ == "__main__":
    main()
