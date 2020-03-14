def main():
    s = int(input())
    i = 1
    save_num = []
    while True:
        i += 1

        if s % 2 == 0:
            s = s // 2
        else:
            s = 3 * s + 1

        if s not in save_num:
            save_num.append(s)
        else:
            ans = i
            break

    print(ans)


if __name__ == "__main__":
    main()
