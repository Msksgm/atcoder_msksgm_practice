import sys


def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    xs.sort()
    ys.sort()
    a = xs[-1]
    b = ys[0]

    if a <= b:
        for i in range(b-a+1):
            z = a + i
            if a < z and z <= b and x < z and z <= y:
                print("No War")
                sys.exit(0)
        print("War")
    else:
        print("War")


if __name__ == "__main__":
    main()
