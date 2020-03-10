def main():
    h, n = map(int, input().split())
    As = list(map(int, input().split()))
    if h <= sum(As):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
