def main():
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    indx = week.index(s)
    diff = 7 - indx
    if diff == 0:
        diff = 7
    print(diff)


if __name__ == "__main__":
    main()
