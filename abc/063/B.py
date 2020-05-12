def main():
    s = list(input())
    q = set(s)
    if len(s) == len(q):
        ans = 'yes'
    else:
        ans = 'no'
    print(ans)


if __name__ == "__main__":
    main()
