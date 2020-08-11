def main():
    a, b = map(int, input().split())
    if b % a == 0:
        ans = b // a
    else:
        ans = (b // a) + 1
    print(ans)


if __name__ == "__main__":
    main()
