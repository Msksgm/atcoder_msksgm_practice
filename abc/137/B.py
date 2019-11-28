def main():
    k, x = map(int, input().split())
    ans = []
    for i in range(-k+1, k):
        ans.append(x+i)
    print(*ans)


if __name__ == "__main__":
    main()
