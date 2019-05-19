
def main():
    R, G, B, N = map(int, [int(x) for x in input().split()])

    c = 0
    for r in range(R+1):
        try:
            N % r == 0
            c += 1
            print(N/r, 0, 0)
        except ZeroDivisionError:
            for g in range(G+1):
                try:
                    (N // r) % g == 0
                    c += 1
                    print(N/r, N/g, 0)
                except ZeroDivisionError:
                    for b in range(B+1):
                        try:
                            ((N // r) // g) % b == 0
                            print(N/r, N/g, N/b)
                            c += 1
                        except ZeroDivisionError:
                            print('Error')

    return print(c)


if __name__ == "__main__":
    main()
