def main():
    x, n = map(int, input().split())
    ps = list(map(int, input().split()))
    anti_ps = [i for i in range(102) if i not in ps]
    anti_ps_abs = [abs(i-x) for i in range(102) if i not in ps]
    ans = anti_ps[anti_ps_abs.index(min(anti_ps_abs))]
    print(ans)


if __name__ == "__main__":
    main()
