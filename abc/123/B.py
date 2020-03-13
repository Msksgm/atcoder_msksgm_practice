import numpy as np


def main():
    dishes = [input() for _ in range(5)]
    first_digit = float("inf")
    order_dishies = []
    print(dishes)
    for i in range(5):
        first_digit = min(int(dishes[i][-1]), first_digit)
        if first_digit == dishes[i][-1]:
            order_dishies.append(i)
        else:
            order_dishies.insert(0, i)
    ans = 0
    for i in range(5):
        if i != 4:
            ans += np.ceil(order_dishies[i])
        else:
            ans += order_dishies[i]
    print(ans)


if __name__ == "__main__":
    main()
