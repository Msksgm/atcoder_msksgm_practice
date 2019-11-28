N, K = map(int, input().split())
pro = 0
for score in range(1, N+1):
    a = 0
    while score < K:
        score *= 2
        a += 1
    pro += 1/N * (0.5**a)
print(pro)
