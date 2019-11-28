# from math import gcd, sqrt
import fractions
import math


def is_prime(n):
    flag = True
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            flag = False
            return

    if flag:
        return n


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def main():
    a, b = map(int, input().split())
    coms = make_divisors(fractions.gcd(a, b))
    ans = [is_prime(i) for i in coms]
    ans2 = [a for a in ans if a is not None]
    print(len(ans2))


if __name__ == "__main__":
    main()
