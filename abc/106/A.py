def main():
    a, b = map(int, input().split())
    ans = a*b - a - b + 1
    print(ans)


if __name__ == "__main__":
    main()
