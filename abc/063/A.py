def main():
    a, b = map(int, input().split())
    ans = a+b
    if ans < 10:
        print(ans)
    else:
        print('error')


if __name__ == "__main__":
    main()
