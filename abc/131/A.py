def main():
    s = list(map(int, list(input())))
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print("Bad")
            import sys; sys.exit(0)
    print("Good")


if __name__ == "__main__":
    main()
