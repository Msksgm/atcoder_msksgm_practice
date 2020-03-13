def main():
    ab = list(map(int, input().split()))
    ans = 0
    for _ in range(2):
        button = max(ab)
        indx = ab.index(button)
        ans += button
        ab[indx] -= 1
    print(ans)


if __name__ == "__main__":
    main()
