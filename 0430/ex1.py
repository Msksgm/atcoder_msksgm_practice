
def main():
    # scanf("%d\n", &a)
    # scanf("%d ", &b)
    # scanf("%d\n", &c)
    # scanf("%c", %s)
    a = input()
    b, c = input().split()
    s = input()

    print("{} {}".format(int(a)+int(b)+int(c), s))


if __name__ == "__main__":
    main()