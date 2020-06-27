def main():
    ss = list(input())
    ts = list(input())
    ans = 0
    for s, t in zip(ss, ts):
        if s != t:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
