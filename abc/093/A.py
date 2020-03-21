def main():
    s = list(input())
    s_num = len(set(s))
    if s_num == 3:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
