import sys


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def main():
    a, b = input().split()
    ab = int(a+b)
    ab_divisor = divisor(ab)
    ab_divisor.remove(1)
    for div in ab_divisor:
        if ab / div == div:
            print('Yes')
            sys.exit(0)

    print('No')


if __name__ == "__main__":
    main()
