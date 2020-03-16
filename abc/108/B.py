def main():
    x1, y1, x2, y2 = map(int, input().split())
    edge_x = x2 - x1
    edge_y = y2 - y1
    x3, y3 = x2 - edge_y, y2 + edge_x
    x4, y4 = x1 - edge_y, y1 + edge_x
    print(x3, y3, x4, y4)


if __name__ == "__main__":
    main()
