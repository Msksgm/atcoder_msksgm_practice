from fractions import gcd


def lcm(c, d):
    return (c * d) // gcd(c, d)


def main():
    a, b, c, d = map(int, input().split())
    c_num = (b//c-(a-1)//c)
    d_num = (b//d-(a-1)//d)
    cd_num = (b//lcm(c, d)-(a-1)//lcm(c, d))
    ans = b-a+1-c_num-d_num+cd_num
    print(ans)


if __name__ == "__main__":
    main()
