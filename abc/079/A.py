def main():
    n = list(map(int, list(input())))

    seqCount = 0
    for i in range(3):
        if seqCount == 2:
            break
        if n[i] == n[i+1]:
            seqCount += 1
        else:
            seqCount = 0

    if seqCount >= 2:
        ans = 'Yes'
    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()
