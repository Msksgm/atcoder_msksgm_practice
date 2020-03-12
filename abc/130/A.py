def main():
    x, a = map(int, input().split())
    if x < a:
        ans = 0
    else:
        ans = 10
    print(ans)


if __name__ == "__main__":
    main()
