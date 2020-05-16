def main():
    n = int(input())
    As = list(map(int, input().split()))

    anss = [0]*n
    for A in As:
        anss[A-1] += 1
    for ans in anss:
        print(ans)


if __name__ == "__main__":
    main()
