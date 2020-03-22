def main():
    a, b, c = map(int, input().split())

    if a+b >= c:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()
