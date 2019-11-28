def main():
    n = 3
    for i in range(2**n):
        print("i=", i)
        for j in range(n):
            print("i >> j", i >> j)
            print("bin(i >> j)", bin(i >> j))
            print("bin(i >> j)&1", (i >> j) & 1)
            if (i >> j) & 1:
                pass
        # print(i)


if __name__ == "__main__":
    main()
