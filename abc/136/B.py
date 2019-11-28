def main():
    N = int(input())

    ans = 0
    if len(str(N)) % 2 == 0:
        for i in range(len(str(N))):
            if i % 2 == 0:
                ans += 9*(10**i)
    else:
        for i in range(len(str(N))+1):
            if i % 2 == 0:
                ans += 9*(10**i)
        ans = ans - (10**len(str(N)) - N) + 1
        
    print(ans)

if __name__ == "__main__":
    main()