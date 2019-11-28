def main():
    n = int(input())
    tapes = [input() for _ in range(n)]

    for tape in tapes:
        count = 0
        i = 0
        while i <= len(tape):
            s = tape[i:i+5]
            if s == "tokyo":
                count += 1
                i += 4
                continue
            if s == "kyoto":
                count += 1
                i += 4
                continue
            i += 1
        print(count)


if __name__ == "__main__":
    main()
