import numpy as np


def my_round(val, digit=0):
    p = 10 ** digit
    return np.ceil((val * p * 2 + 1)) // 2 / p


def main():
    dishes = [input() for _ in range(5)]
    first_digit = float("inf")
    order_dishies = []
    for i in range(5):
        if int(dishes[i][-1]) == 0:
            order_dishies.insert(0, i)
        else:
            first_digit = min(int(dishes[i][-1]), first_digit)
            if first_digit == int(dishes[i][-1]):
                order_dishies.append(i)
            else:
                order_dishies.insert(0, i)
    ans = 0
    for i in range(5):
        if i == 4:
            ans += int(dishes[order_dishies[i]])
        else:
            ans += my_round(int(dishes[order_dishies[i]]), -1)
    print(int(ans))


if __name__ == "__main__":
    main()
