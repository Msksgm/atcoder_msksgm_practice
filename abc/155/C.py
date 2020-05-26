def main():
    n = int(input())
    ss = {}
    max_s = 0
    for _ in range(n):
        s = input()
        if s not in ss:
            ss[s] = 0
        else:
            ss[s] += 1
            max_s = max(max_s, ss[s])

    ss = sorted(ss.items(), key=lambda x: x[0])
    anss = [s for s, i in ss if i == max_s]
    for ans in anss:
        print(ans)


if __name__ == "__main__":
    main()
