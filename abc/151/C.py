def main():
    from sys import stdin
    input = stdin.readline
    N, M = map(int, input().split())
    SP = [tuple(input().split()) for i in range(M)]
    wa_num_temp = {}
    ac_num_temp = {}
    for sp in SP:
        if sp[0] in list(ac_num_temp.keys()):
            continue
        if sp[0] not in list(wa_num_temp.keys()):
            wa_num_temp[sp[0]] = 0
        if sp[1] == "WA":
            wa_num_temp[sp[0]] += 1
        elif sp[1] == "AC":
            ac_num_temp[sp[0]] = 1

    print(sum(ac_num_temp.values()), sum(wa_num_temp.values()))


if __name__ == "__main__":
    main()
