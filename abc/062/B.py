def main():
    b, w = map(int, input().split())
    image = [list(input()) for _ in range(b)]
    image.insert(0, ["#"]*w)
    image.append(["#"]*w)
    for im in image:
        im.insert(0, "#")
        im.append("#")

    for im in image:
        print(*im, sep="")


if __name__ == "__main__":
    main()
