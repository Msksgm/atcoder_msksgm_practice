def main():
    n = int(input())
    ls = list(map(int, input().split()))

    long_edge = max(ls)
    ls.remove(long_edge)
    if long_edge < sum(ls):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
