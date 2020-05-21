def main():
    n = int(input())
    s = list(input())

    ans = s.count("R")*s.count("G")*s.count("B")
    for i in range(n):
        for j in range(i+1, n):
            k = j + j - i
            if k < n and s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
