def main():
    n = int(input())
    s = list(input())

    ans = 0
    for i in range(n-2):
        abc = str(s[i]) + str(s[i+1]) + str(s[i+2])
        if abc == "ABC":
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
