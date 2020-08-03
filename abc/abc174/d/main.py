def main():
    n = int(input())
    cs = input()
    color_list = []
    for i in range(n):
        if cs[i] == "W":
            color_list.append(0)
        else:
            color_list.append(1)
    r_count = sum(color_list)
    ans = r_count - sum(color_list[:r_count])
    print(ans)


if __name__ == "__main__":
    main()
