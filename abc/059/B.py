def main():
    a = int(input())
    b = int(input())
    if a > b:
        ans = "GREATER"
    elif a < b:
        ans = "LESS"
    else:
        ans = "EQUAL"
    print(ans)


if __name__ == "__main__":
    main()
