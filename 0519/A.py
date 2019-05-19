
def main():
    N, K = map(int, [int(x) for x in input().split()])
    S = input()

    ans = ""
    for i, n in enumerate(S):
        if i == K-1:
            n = n.lower()
        ans += n
    print(ans)
    return ans


if __name__ == "__main__":
    main()
