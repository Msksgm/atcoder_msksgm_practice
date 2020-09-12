from collections import deque


def main():
    ss = list(input())
    ans = deque([])
    for s in ss:
        if s == '0':
            ans.append(s)
        elif s == '1':
            ans.append(s)
        else:
            if len(ans) == 0:
                pass
            else:
                ans.pop()
    print(*list(ans), sep='')


if __name__ == "__main__":
    main()
