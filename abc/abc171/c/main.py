def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return int(X % n)


def main():
    n = int(input())
    alphabets = list(chr(i)for i in range(97, 123))
    ans = ''
    while n != 0:
        n -= 1
        ans += alphabets[n % 26]
        n //= 26
    print(ans[::-1])


if __name__ == "__main__":
    main()
