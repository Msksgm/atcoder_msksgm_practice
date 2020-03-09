def main():
    st = input().split()
    ab = list(map(int, input().split()))
    u = input()

    indx = st.index(u)
    ab[indx] -= 1
    a, b = ab
    print(a, b)


if __name__ == "__main__":
    main()
