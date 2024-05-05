def main() -> None:
    N = int(input())
    restaurants = [tuple(input().split() + [i+1]) for i in range(N)]
    restaurants = sorted(restaurants, key=lambda x: (x[0], -int(x[1])))

    for r in restaurants:
        print(r[2])


if __name__ == "__main__":
    main()