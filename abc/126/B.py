
def main():
    S = input()

    A = int(S[:2])
    B = int(S[2:])

    if A != 0 and B <= 12 and B != 0 and A <= 12:
        print("AMBIGUOUS")

    elif (A != 0 and B <= 12) and B != 0:
        print("YYMM")

    elif (B != 0 and A <= 12) and A != 0:
        print("MMYY")

    elif (A == 0 and 1 <= B and B <= 12):
        print("YYMM")

    elif (B == 0 and 1 <= A and A <= 12):
        print("MMYY")

    else:
        print("NA")


if __name__ == "__main__":
    main()
