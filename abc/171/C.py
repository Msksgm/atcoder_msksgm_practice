def main():
    alphabet = list(chr(i)for i in range(97, 123))
    n = int(input())
    ans = ''
    while n > 0:
        n -= 1
        ans = chr(ord('a') + (n % 26)) + ans
        n = n//26

    print(ans)


if __name__ == "__main__":
    main()
