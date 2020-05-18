from collections import deque


def bfs(rooms, v=1):
    arrow = [-1] * len(rooms)
    q = deque()
    q.append(v)

    while q:
        now = q.popleft()
        for next_v in rooms[now]:
            if arrow[next_v] != -1:
                continue
            else:
                q.append(next_v)
                arrow[next_v] = now
    return arrow


def main():
    n, m = map(int, input().split())
    rooms = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        rooms[b].append(a) 
        rooms[a].append(b)

    anss = bfs(rooms)
    print("Yes")
    for ans in anss[2:]:
        print(ans)


if __name__ == "__main__":
    main()
