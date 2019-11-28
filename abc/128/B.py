def main():
    N = int(input())
    SP = [list(input().split()) for i in range(N)]
    for i, SPl in enumerate(SP):
        SPl.append(i+1)
        SPl[1] = int(SPl[1])
    # print(SP)
    SP.sort(reverse=True, key=lambda x: x[1])
    # print(SP)
    SP.sort(key=lambda x: x[0])
    # print(SP)

    for sp in SP:
        print(sp[2])


if __name__ == "__main__":
    main()
