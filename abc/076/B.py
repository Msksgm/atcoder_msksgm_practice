def main():
    n = int(input())
    k = int(input())
    ans = 1

    for i in range(n):
        if ans * 2 < ans + k:
            ans = ans * 2
        else:
            ans = ans + k
    print(ans)


if __name__ == "__main__":
    main()
