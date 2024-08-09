def main() -> None:
    N = int(input())
    S = input()

    win_dict = {"R": "P", "S": "R", "P": "S"}
    lose_dict = {"R": "S", "S": "P", "P": "R"}
    dp = [{"R": 0, "S": 0, "P": 0}]

    for i in range(N):
        pre = dp[i]
        win = win_dict[S[i]]
        draw = S[i]
        lose = lose_dict[S[i]]
        if win == "R":
            current = {"R": max(pre[draw], pre[lose]) + 1, "S": max(pre[win], pre[lose]), "P": 0}
        if win == "S":
            current = {"S": max(pre[draw], pre[lose]) + 1, "P": max(pre[win], pre[lose]), "R": 0}
        if win == "P":
            current = {"P": max(pre[draw], pre[lose]) + 1, "R": max(pre[win], pre[lose]), "S": 0}
        dp.append(current)

    print(max(dp[N].values()))

if __name__ == "__main__":
    main()