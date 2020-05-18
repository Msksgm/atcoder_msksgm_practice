def search(rooms, li, anss, count):
    count += 1
    for l in li:
        if anss[l] == 0:
            anss[l] = count
            search(rooms, rooms[l], anss, count)
    return anss


def main():
    n, m = map(int, input().split())
    rooms = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        rooms[b].append(a) 
        rooms[a].append(b)
    anss = [0]*(n+1)
    li = rooms[1]
    count = 0
    anss = search(rooms, li, anss, count)
    if 0 in anss[1:]:
        print("No")
    else:
        print("Yes")
        for ans in anss[1:]:
            print(ans)


if __name__ == "__main__":
    main()
