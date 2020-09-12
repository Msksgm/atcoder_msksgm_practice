def main():
    n = int(input())
    As = list(map(int, input().split()))
    nums2As = [[i+1, As[i]] for i in range(n)]
    nums2As_sort = sorted(nums2As, key=lambda x: -x[1])
    for i in range(n):
        print(nums2As_sort[i][0])


if __name__ == "__main__":
    main()
