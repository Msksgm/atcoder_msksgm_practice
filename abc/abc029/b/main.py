def main():
    ans = 0
    for _ in range(12):
        s = input()
        if "r" in s:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
