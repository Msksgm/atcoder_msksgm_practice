def main():
    cs = [list(input()) for _ in range(2)]
    ul = cs[0][0]
    uc = cs[0][1]
    ur = cs[0][2]
    bl = cs[1][0]
    bc = cs[1][1]
    br = cs[1][2]

    if ul == br and uc == bc and ur == bl:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)


if __name__ == "__main__":
    main()
