def main():
    As = list(map(int, input().split()))
    if sum(As) >= 22:
        print('bust')
    else:
        print('win')


if __name__ == "__main__":
    main()
