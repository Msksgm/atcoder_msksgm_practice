def main():
    s = input()
    k = int(input())

    n = len(s)
    ans_list = []
    if k > n:
        pass
    else:
        for i in range(n-k+1):
            ans_list.append(s[i:i+k])

    ans = len(set(ans_list))
    print(ans)


if __name__ == "__main__":
    main()
