def main():
    n = int(input())
    ss = list(input())

    ans = ''
    for s in ss:
        ans_temp = ord(s) + n
        if ord('A') <= ans_temp <= ord('Z'):
            ans += chr(ans_temp)
        if ans_temp < ord("A"):
            ans += chr(ord('Z') - (ord("A") - ans_temp) - 1)
        if ans_temp > ord('Z'):
            ans += chr(ord("A") + (ans_temp - ord('Z')) - 1)

    print(ans)


if __name__ == "__main__":
    main()
