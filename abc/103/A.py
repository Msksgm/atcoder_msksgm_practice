from itertools import permutations as per


def main():
    a1, a2, a3 = map(int, input().split())
    As = list(per([a1, a2, a3], 3))
    ans = float("inf")
    for A in As:
        ans = min(ans, abs(A[0] - A[1])+abs(A[1] - A[2]))

    print(ans)


if __name__ == "__main__":
    main()
