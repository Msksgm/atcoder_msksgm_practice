def main():
    n = int(input())
    b = [i for i in map(int, input().split())]
    b.append(max(b)+1)
    a = []
    for j, num in enumerate(b):
        a.append(min(b[j-1], b[j]))

    print(sum(a))


if __name__ == "__main__":
    main()
