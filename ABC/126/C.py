def main() -> None:
    N, K = map(int, input().split())

    win_rate = []

    for i in range(1, N+1):
        count = 0
        point = i
        while point < K:
            count += 1
            point *= 2
        win_rate.append((1/2) ** count)

    ans = sum(win_rate) / len(win_rate)
    print(ans)


if __name__ == "__main__":
    main()