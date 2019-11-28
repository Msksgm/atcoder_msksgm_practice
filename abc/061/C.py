def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(2**(n-1)):
        num = ""
        # print("pattern{}: ".format(i), end="")
        # print("a")
        for j in range(n):
            num += s[j]
            if ((i >> j) & 1):
                num += "+"
        # print(eval(num))
        ans += eval(num)
    print(ans)


if __name__ == "__main__":
    main()
