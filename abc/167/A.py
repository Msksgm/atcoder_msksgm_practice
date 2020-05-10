def main():
    s = input()
    t = input()
    if s == t[:-1]:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
