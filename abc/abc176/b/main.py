def main():
    ns = list(map(int, list(input())))
    if sum(ns) % 9 == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
