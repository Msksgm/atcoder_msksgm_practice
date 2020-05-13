def main():
    a, b, c = map(int, input().split())
    add = a
    mods = [0]*b
    i = a % b
    while mods[i] == 0:
        mods[i] = 1
        if i == c:
            print('YES')
            exit()
        a = a+add
        i = a % b
    print('NO')


if __name__ == "__main__":
    main()
