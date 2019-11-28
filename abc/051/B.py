def main():
    k, s = map(int, input().split())
    # print(k, s)
    ans = 0
    for z in range(k+1):
        if z <= s:
            for y in range(k+1):
                x = s - z - y
                if 0 <= x and x <= s and x <= k:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
