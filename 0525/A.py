
def main():
    A, B = map(int, input().split())

    if A <= 5:
        print("0")

    elif 6 <= A and A <= 12:
        print("{}".format(B//2))

    else:
        print("{}".format(B))


if __name__ == "__main__":
    main()
