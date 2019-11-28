def main():
    N, M = map(int, input().split())
    box = []
    for i in range(M):
        LR = [j for j in map(int, input().split())]
        box += LR

    # print(box)
    num = 0
    for j in range(1, N+1):
        plus = 1
        # print(j)
        if plus == 1:
            for i in range(0, len(box), 2):
                # print(box[i], box[i+1])
                if j < box[i] or box[i+1] < j:
                    plus = 0
                    break

            num += plus

    print(num)


if __name__ == "__main__":
    main()
