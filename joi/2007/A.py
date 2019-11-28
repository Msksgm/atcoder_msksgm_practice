def main():
    price = int(input())
    charge = 1000 - price

    ans = 0

    while charge != 0:
        # print(charge)
        if charge - 500 >= 0:
            charge = charge - 500
            ans += 1
        elif charge - 100 >= 0:
            charge = charge - 100
            ans += 1
        elif charge - 50 >= 0:
            charge = charge - 50
            ans += 1
        elif charge - 10 >= 0:
            charge = charge - 10
            ans += 1
        elif charge - 5 >= 0:
            charge = charge - 5 
            ans += 1
        else:
            ans += charge
            charge = 0
    print(ans)


if __name__ == "__main__":
    main()
