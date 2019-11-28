from collections import Counter


def main():
    n, k, q = map(int, input().split())
    a = Counter([int(input()) for _ in range(q)])
    p = [0 for _ in range(n)]
    for key, v in a.items():
        p[key-1] += v

    for s in p:
        if s-q <= -k:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
