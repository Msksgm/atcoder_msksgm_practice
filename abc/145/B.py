def main():
    n = int(input())
    s = list(input())
    if n % 2 != 0:
        print("No")
    else:
        div = n // 2
        if s[:div-1] == s[div:n-1]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
