def main():
    a, b = map(int, input().split())
    diff = abs(max(b, a) - min(a, b))
    if diff % 2 != 0:
        print("IMPOSSIBLE")
    else:
        bigger = max(a, b)
        ans = bigger - (diff//2)
        print(ans)


if __name__ == "__main__":
    main()
