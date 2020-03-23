def main():
    n = int(input())
    ss = list(input().split())

    ss_set = set(ss)
    if len(ss_set) == 3:
        ans = "Three"
    else:
        ans = "Four"

    print(ans)


if __name__ == "__main__":
    main()
