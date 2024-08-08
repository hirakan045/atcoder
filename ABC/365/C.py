def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if sum(A) <= M:
        print("infinite")
    else:
        low = 0
        high = 10 ** 9 + 1
        while high - low >= 2:
            mid = (low + high) // 2
            cost = 0
            for a in A:
                cost += min(mid, a)
            if cost <= M:
                low = mid
            else:
                high = mid
        print(low)

if __name__ == "__main__":
    main()