def main():
    a, b, c = map(int, input().split())
    mod = 1000000007
    ans = (a*b*c) % (mod)
    print(ans)


if __name__ == "__main__":
    main()
