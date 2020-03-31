def main():
    n = input()
    n_int = int(n)
    n_li = list(map(int, list(n)))
    n_sum = sum(n_li)

    if n_int % n_sum == 0:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()
