def main():
    a, b = input().split()
    A = a*int(b)
    B = b*int(a)
    ans = sorted([A, B])
    print(ans[0])


if __name__ == "__main__":
    main()