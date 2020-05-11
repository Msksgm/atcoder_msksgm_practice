def main():
    n = int(input())

    i = 0
    ans = 1
    while 2**i < n:
        i += 1
    if 2**i == n:
        ans = 2**i
    else:
        ans = 2**(i-1)
    print(ans)


if __name__ == "__main__":
    main()
