def main():
    k = int(input())
    s = list(input())
    n = len(s)
    if n > k:
        print(*s[:k], "...", sep="")
    else:
        print(*s, sep="")


if __name__ == "__main__":
    main()
