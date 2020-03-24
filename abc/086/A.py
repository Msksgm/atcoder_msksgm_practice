def main():
    a, b = map(int, input().split())
    if a*b % 2 == 0:
        ans = 'Even'
    else:
        ans = 'Odd'
    print(ans)


if __name__ == "__main__":
    main()
