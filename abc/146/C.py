def is_ok(N, A, B, X):
    return A*N + B*len(str(N)) <= X


def main():
    a, b, x = map(int, input().split())

    left = 0
    right = 10**9 + 1
    while right - left > 1:
        mid = (right + left) // 2
        if is_ok(mid, a, b, x):
            left = mid
        else:
            right = mid
    print(left)


if __name__ == "__main__":
    main()
