def main():
    n1, n2, n3, n4 = list(input())
    if n1 == n2 and n2 == n3 and n3 == n4:
        ans = 'SAME'
    else:
        ans = 'DIFFERENT'
    print(ans)


if __name__ == "__main__":
    main()
