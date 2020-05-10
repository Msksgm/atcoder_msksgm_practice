def main():
    s = list(input())
    li = list(chr(i)for i in range(97, 123))
    for i in li:
        if i not in s:
            print(i)
            exit()
    print('None')


if __name__ == "__main__":
    main()
