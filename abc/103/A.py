def main():
    a1, a2, a3 = map(int, input().split())
    ans = max(abs(a1 - a2), abs(a2 - a3))
    print(ans)


if __name__ == "__main__":
    main()
