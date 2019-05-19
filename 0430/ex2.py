def main():

    A, B, T = input().split()

    c = (int(T) + 0.5) // int(A)
    ans = c * int(B)

    print(int(ans))


if __name__ == "__main__":
    main()