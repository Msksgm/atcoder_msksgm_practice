def main():
    A = int(input())
    B = int(input())
    for i in range(3):
        if i + 1 == A or i + 1 == B:
            continue
        else:
            print(i+1)


if __name__ == "__main__":
    main()
