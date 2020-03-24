def main():
    a, b = map(int, input().split())
    s = input()

    if s[a] != '-':
        print('No')
    else:
        if s[:a].isdigit() and s[b:].isdigit():
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
