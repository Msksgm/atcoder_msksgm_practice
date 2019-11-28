def main():
    s = input()

    for i, a in enumerate(s):
        if i % 2 == 0:
            if a == "L":
                print("No")
                break
        else:
            if a == "R":
                print("No")
                break
        if len(s) == i+1:
            print("Yes")


if __name__ == "__main__":
    main()
