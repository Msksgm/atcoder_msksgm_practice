import sys


def main():
    n = int(input())
    As = list(map(int, input().split()))
    for A in As:
        if A % 2 != 0:
            continue
        if A % 3 == 0 or A % 5 == 0:
            continue
        print("DENIED")
        sys.exit(0)
    print("APPROVED")


if __name__ == "__main__":
    main()
