from itertools import permutations as perm


def euclidean_distance(list1, list2):
    x_norm = (list1[0] - list2[0]) ** 2
    y_norm = (list1[1] - list2[1]) ** 2
    return (x_norm + y_norm) ** 0.5


def main():
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]

    orders = list(perm([xys[i] for i in range(n)], n))
    order_num = len(orders)
    ans = 0
    for order in orders:
        for i in range(n-1):
            ans += euclidean_distance(order[i], order[i+1])

    print(ans/order_num)


if __name__ == "__main__":
    main()
