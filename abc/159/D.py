from collections import Counter


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = Counter(arr)
    total = 0
    for key in cnt.keys():
        total += cnt[key]*(cnt[key]-1)//2

    for i in range(n):
        tmp = total
        tmp -= cnt[arr[i]]*(cnt[arr[i]]-1)//2
        tmp += (cnt[arr[i]]-1)*(cnt[arr[i]]-2)//2
        print(tmp)


if __name__ == "__main__":
    main()
