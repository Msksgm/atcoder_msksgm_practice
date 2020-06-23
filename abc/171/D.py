def main():
    n = int(input())

    As = list(map(int, input().split()))
    nums = [0] * (10**5+1)
    ans = 0
    for a in As:
        ans += a
        nums[a] += 1

    q = int(input())
    for i in range(q):
        b, c = map(int, input().split())
        ans += (c-b) * nums[b]
        nums[c] += nums[b]
        nums[b] = 0
        print(ans)


if __name__ == "__main__":
    main()
