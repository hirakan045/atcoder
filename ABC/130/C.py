def main() -> None:
    W, H, x, y = map(int, input().split())

    S = W * H

    if x == W / 2 and y == H / 2:
        print(S/2, 1)
    else:
        print(S/2, 0)

if __name__ == "__main__":
    main()