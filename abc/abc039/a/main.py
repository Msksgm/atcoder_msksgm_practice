def main():
    a, b, c = map(int, input().split())
    ans = ((a*b)+(b*c)+(c*a))*2
    print(ans)


if __name__ == "__main__":
    main()
