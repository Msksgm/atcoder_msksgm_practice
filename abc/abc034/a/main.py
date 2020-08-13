def main():
    x, y = map(int, input().split())
    if y > x:
        ans = "Better"
    else:
        ans = "Worse"
    print(ans)


if __name__ == "__main__":
    main()
