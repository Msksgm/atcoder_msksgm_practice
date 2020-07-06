def main():
    n = int(input())
    results = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
    for i in range(n):
        s = input()
        results[s] += 1

    for result, num in results.items():
        print("{} x {}".format(result, num))


if __name__ == "__main__":
    main()
