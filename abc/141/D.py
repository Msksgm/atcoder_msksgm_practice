from collections import Counter


def main():
    n, m = map(int, input().split())
    a = sorted([int(i) for i in input().split()])
    a = a[::-1]

    ans = []
    if len(a) != 1:
        for j in range(len(a)):
            # if m == 0:
            #     ans.append(a[j])
            # else:
            for k in range(1, m+1):
                adds = int(a[j] / (2**(k)))
                if int(a[j]/(2**(k+1))) == 1:
                    break
            print("k=", k)
            m -= k
            print("m=", m)
            ans.append(adds)
    else:
        for k in range(1, m+1):
            adds = int(a[0] / (2**(k)))

    # print(n, m)
    # print(a)
    print(ans)
    print(sum(ans))


if __name__ == "__main__":
    main()
