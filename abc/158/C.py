def main():
    a, b = map(int, input().split())
    a_temp = int(a/0.08)
    b_temp = int(b/0.1)
    if max(a_temp, b_temp) == a_temp:
        if int(a_temp*0.1) == b:
            ans = a_temp
        else:
            ans = -1
    else:
        if int(b_temp*0.08) == a:
            ans = b_temp
        else:
            ans = -1
    print(ans)


if __name__ == "__main__":
    main()
