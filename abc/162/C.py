from math import gcd


def main():
    k = int(input())

    ans = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            s = gcd(i, j)
            for h in range(1, k+1):
                ans += gcd(s, h)
    print(ans)


if __name__ == "__main__":
    main()
