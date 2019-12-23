def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 1
    ans = 0
    for i in range(N):
        if a[i] == count:
            count += 1
            continue
        else:
            ans += 1

    if count == 1 and ans != 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
