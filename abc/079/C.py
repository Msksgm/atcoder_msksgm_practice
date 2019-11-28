def main():
    abcd = input()
    n = len(abcd)
    for i in range(2**(n-1)):
        num = ""
        # print(i)
        for j in range(n):
            num += abcd[j]
            if j < n-1:
                if (i >> j) & 1:
                    num += "-"
                else:
                    num += "+"
        if eval(num) == 7:
            print(num+"=7")
            exit()


if __name__ == "__main__":
    main()
