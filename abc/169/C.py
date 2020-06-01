def main():
    a, b = input().split()
    a = int(a)
    b0 = int(b[0])*100
    b1 = int(b[2])*10
    b2 = int(b[3])
    ans = (a*b0 + a*b1 + a*b2)//100
    print(ans)


if __name__ == "__main__":
    main()
