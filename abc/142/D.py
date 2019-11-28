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
    a, b = make_divisors(a), make_divisors(b)
    a.extend(b)
    print(a)
    dup = [x for x in set(a) if a.count(x) > 1]
    print(dup)

if __name__ == "__main__":
    main()
