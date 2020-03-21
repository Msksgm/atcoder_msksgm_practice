def main():
    a, b, c = map(int, input().split())
    k = int(input())

    abc = [a, b, c]
    max_index = abc.index(max(a, b, c))
    ans = 0
    for i in range(3):
        num = abc[i]
        if i == max_index:
            for _ in range(k):
                num *= 2
            ans += num
        else:
            ans += num

    print(ans)


if __name__ == "__main__":
    main()
