def main():
    n, m = map(int, input().split())
    kas = [list(map(int, input().split())) for _ in range(n)]
    question_dict = {i: 0 for i in range(1, m+1)}
    ans = 0

    for ka in kas:
        a = ka[1:]
        for i in a:
            question_dict[i] += 1

    for food, num in question_dict.items():
        if num == n:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
