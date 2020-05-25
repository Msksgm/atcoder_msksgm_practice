from collections import Counter


def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    max_num = Counter(ss).most_common()[0][1]
    max_verbs = [Counter(ss).most_common()[0][0]]
    for i in range(1, len(Counter(ss).most_common())):
        if Counter(ss).most_common()[i][1] != max_num:
            break
        max_verbs.append(Counter(ss).most_common()[i][0])

    max_verbs = sorted(max_verbs)
    for ans in max_verbs:
        print(ans)


if __name__ == "__main__":
    main()
