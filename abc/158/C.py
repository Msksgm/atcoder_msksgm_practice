def main():
    a, b = map(int, input().split())
    ans = -1
    for i in range(10000, -1, -1):
        tax1 = int(i*0.08)
        tax2 = int(i*0.10)
        if tax1 == a and tax2 == b:
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
