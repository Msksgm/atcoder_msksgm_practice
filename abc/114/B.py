def main():
    s = input()
    n = len(s)
    ans = float("inf")
    for i in range(n-2):
        if ans > abs(753 - int(s[i:i+3])):
            ans = abs(753 - int(s[i:i+3]))
    print(ans)


if __name__ == "__main__":
    main()
