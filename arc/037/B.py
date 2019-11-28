
def dfs(vs):
    check = []
    edges = []
    for i in vs:
        print(i)
    while vs:
        h, w = vs.pop(0)
        edges.append(h)
        if w in check:
            continue
        else
            for v in vs:
                if v[0] == h:
                    



def main():
    n, m = map(int, input().split())
    vs = [list(map(int, input().split())) for _ in range(m)]

    print(n, m)
    print(vs)
    dfs(vs)


if __name__ == "__main__":
    main()
