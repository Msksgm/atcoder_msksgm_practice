def main():
    x = int(input())
    ans = 0
    m = 100
    while True:
        if m >= x:
            print(ans)
            exit()
        else:
            m = m + int(m * 0.01)
            ans += 1


if __name__ == "__main__":
    main()
