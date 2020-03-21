def main():
    n = input()
    n_int = int(n)
    n_list = map(int, list(n))
    sn = sum(n_list)

    if n_int % sn == 0:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
