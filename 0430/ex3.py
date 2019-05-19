def main():
    N = input()

    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    V_sum = 0
    C_sum = 0
    for i, j in zip(V, C):
        if i - j > 0:
            # print(i, j)
            V_sum += i
            C_sum += j

    print(V_sum-C_sum)


if __name__ == "__main__":
    main()
