def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    ans = len(set(ss))
    print(ans)


if __name__ == "__main__":
    main()
