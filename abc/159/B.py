def main():
    s = list(input())

    n = len(s)
    left = s[:(n-1)//2]
    right = s[(n+1)//2:]

    if left == right:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
