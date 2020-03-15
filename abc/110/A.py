def main():
    abc = list(map(int, input().split()))
    abc.sort(reverse=True)
    ans = int(str(abc[0]) + str(abc[1])) + abc[2]
    print(ans)


if __name__ == "__main__":
    main()
