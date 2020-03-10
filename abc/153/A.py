def main():
    h, a = map(int, input().split())
    ans = 0
    while True:
        h = h-a
        ans += 1
        if h <= 0:
            break
    print(ans)


if __name__ == "__main__":
    main()
