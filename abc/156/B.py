def ans(n, k):
    if (int(n/k)):
        return ans(int(n/k), k)+str(n % k)
    return str(n % k)


def main():
    n, k = map(int, input().split())
    print(len(ans(n, k)))


if __name__ == "__main__":
    main()
