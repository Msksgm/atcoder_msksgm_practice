def main():
    n = int(input())
    if n <= 59:
        ans = 'Bad'
    elif 60 <= n and n <= 89:
        ans = 'Good'
    elif 90 <= n and n <= 99:
        ans = 'Great'
    else:
        ans = 'Perfect'
    print(ans)


if __name__ == "__main__":
    main()
