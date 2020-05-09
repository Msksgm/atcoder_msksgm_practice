def main():
    s = list(input())
    s = sorted(set(s))
    ans = 'None'
    for i in range(len(s)-1):
        if ord(s[i])+1 != ord(s[i+1]):
            ans = chr(ord(s[i])+1)
            break
    print(ans)


if __name__ == "__main__":
    main()
