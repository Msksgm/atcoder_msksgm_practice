def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ans = 0
    for i in range(n-2):
        temp_sort = sorted(ps[i:i+3])
        if ps[i+1] == temp_sort[1]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
