def main():
    r, D, x = map(int, input().split())

    for i in range(10):
        x = r * x - D
        print("{}".format(x))


if __name__ == "__main__":
    main()
