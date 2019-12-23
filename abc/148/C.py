from fractions import gcd


def main():
    A, B = map(int, input().split())
    AB = gcd(A, B)
    ans = (A * B) // AB
    print(ans)


if __name__ == "__main__":
    main()
