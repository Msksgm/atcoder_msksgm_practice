def main():
    ss = list(input())
    r_count = ss.count("R")
    if r_count == 2 and ss[0] == "R" and ss[2] == "R":
        ans = 1
    else:
        ans = r_count
    print(ans)


if __name__ == "__main__":
    main()
