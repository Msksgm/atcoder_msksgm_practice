def main():
    x, y = map(int, input().split())
    for i in range(x+1):
        j = x - i
        if i*4 + j*2 == y:
            print("Yes")
            exit()
        if i*2 + j*4 == y:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
