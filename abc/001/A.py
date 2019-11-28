import math


def main():
    h, w = map(int, input().split())
    cs = [input() for _ in range(h)]
    stack = ["s"]
    check = ["s"]
    print(cs)
    for i in range(h):
        if "s" in cs[i]:
            hnow, wnow = i, cs[i].index("s")
    hnow2, wnow2 = hnow, wnow
    print(hnow, wnow)
    count = 0
    while 1:
        count += 1
        print("stack", stack)
        print("check", check)
        for k in range(h):
            if stack[-1] in cs[k]:
                hnow, wnow = k, cs[k].index(stack[-1])
        print(hnow, wnow)
        if len(stack) != 0:
            if stack[-1] == "g":
                print("Yes")
                # exit()
                break
        stack.pop()
        if hnow < h-1:
            if cs[hnow+1][wnow] != "#":
                if cs[hnow+1][wnow] not in stack:
                    stack.extend(cs[hnow+1][wnow])
                    check.append(cs[hnow+1][wnow])
        if wnow < w-1:
            if cs[hnow][wnow+1] != "#":
                if cs[hnow][wnow+1] not in stack:
                    stack.extend(cs[hnow][wnow+1])
                    check.append(cs[hnow][wnow+1])
        if hnow > 0:
            if cs[hnow-1][wnow] != "#":
                if cs[hnow-1][wnow] not in stack:
                    stack.extend(cs[hnow-1][wnow])
                    check.append(cs[hnow-1][wnow])
        if wnow > 0:
            if cs[wnow][wnow-1] != "#":
                if cs[hnow][wnow-1] not in stack:
                    stack.extend(cs[hnow][wnow-1])
                    check.append(cs[hnow][wnow-1])
        import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()
