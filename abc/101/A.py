def main():
    ss = list(input())
    ans = 0
    for s in ss:
        if s == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
