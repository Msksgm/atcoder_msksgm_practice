import math


def lcm(a, b):
    return (a * b) // (math.gcd(a, b))


def main():
    a = int(input())
    b = int(input())
    n = int(input())
    ans_temp = lcm(a, b)
    ans = 0
    while True:
        if ans >= n:
            break
        ans += ans_temp
    print(ans)


if __name__ == "__main__":
    main()
