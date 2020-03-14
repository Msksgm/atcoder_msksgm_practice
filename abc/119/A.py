def main():
    s = input()
    y, m, d = map(int, s.split("/"))
    if m > 4:
        print("TBD")
    else:
        print("Heisei")


if __name__ == "__main__":
    main()
