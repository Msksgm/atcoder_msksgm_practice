def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    A.sort()  # 連続の整数をソート
    BC.sort(reverse=True, key=lambda x: x[1])  # 数を大きい順にソート

    # print(BC)
    C = []
    for bc in BC:
        # print(bc)
        C += [bc[1]] * bc[0]
        # print(C)
        if len(C) > N:
            print(len(C))
            break

    print(A)
    print(C)
    score = sum(A)
    print(score)
    ans = score
    for i in range(N):
        if i >= len(C):
            break
        print("A[{}], C[{}]".format(i, i))
        print(A[i], C[i])
        score = score - A[i] + C[i]
        ans = max(ans, score)
        print(ans)

    print(ans)


if __name__ == "__main__":
    main()
