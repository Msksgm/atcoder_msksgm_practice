def main():
    S = list(input())
    ret = len(S)
    ans = 0
    for i in range(ret//2):
        if S[i] != S[ret-i-1]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
