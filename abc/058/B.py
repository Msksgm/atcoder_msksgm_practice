def main():
    o = list(input())
    e = list(input())

    ans = ''
    if len(o) == len(e):
        for i in range(len(o)):
            ans += o[i]+e[i]
    else:
        for i in range(len(o)-1):
            ans += o[i]+e[i]
        ans += o[-1]
    print(ans)


if __name__ == "__main__":
    main()
