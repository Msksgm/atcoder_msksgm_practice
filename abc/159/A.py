from itertools import combinations as comb


def main():
    n, m = map(int, input().split())

    n_list = list(range(n))
    m_list = list(range(m))
    n_pair = list(comb(n_list, 2))
    m_pair = list(comb(m_list, 2))
    ans = len(n_pair) + len(m_pair)
    print(ans)


if __name__ == "__main__":
    main()
