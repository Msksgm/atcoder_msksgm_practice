import heapq


def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab = sorted(ab)
    # print(n, m)
    # print(ab)
    index = 0
    ans = []
    money = 0
    for day in range(1, m+1):
        # print(day)
        while index < n and ab[index][0] <= day:
            heapq.heappush(ans, -ab[index][1])
            index += 1
            # print(ans)
        if ans:
            money -= heapq.heappop(ans)

    print(money)


if __name__ == "__main__":
    main()
