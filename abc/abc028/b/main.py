def main():
    ss = list(input())
    counter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
    ans = [0, 0, 0, 0, 0, 0]

    for s in ss:
        ans[counter[s]] += 1

    print(*ans, end="\n")


if __name__ == "__main__":
    main()
