def main():
    h = int(input())

    if h == 1:
        print(1)
        exit()

    for i in range(40):
        if 2**(i+1) == h:
            n = i+2
            break
        if 2**(i) < h and h < 2**(i+1):
            n = i+1
            break
    ans = sum([2**i for i in range(n)])
    print(ans)


if __name__ == "__main__":
    main()
