def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    n = int(input())
    As = list(map(int, input().split()))

    ans = float("inf")
    for i in range(n):
        if factorization(As[i])[0][0] != 2:
            ans = 0
            break
        else:
            ans = min(ans, factorization(As[i])[0][1])
    print(ans)


if __name__ == "__main__":
    main()
