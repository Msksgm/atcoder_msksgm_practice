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
    n = int(input())
    divs = sorted(divisor(n))
    if len(divs) % 2 == 0:
        left = len(divs)//2 - 1
        right = len(divs)//2
    else:
        left, right = len(divs)//2, len(divs)//2

    ans = divs[left] + divs[right] - 2
    print(ans)


if __name__ == "__main__":
    main()
