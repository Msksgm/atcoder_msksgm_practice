def main():
    n = int(input())
    As = list(map(int, input().split()))
    As.insert(0, 0)
    As.append(0)
    print(As)
    route_sum = 0
    for i in range(n):
        route_sum += abs(As[i] - As[i+1])
    print(route_sum)


if __name__ == "__main__":
    main()
