def main() -> None:
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    left = 0
    current_sum = 0
    count = 0

    for right in range(N):
        current_sum += A[right]

        while current_sum >= K:
            count += (N - right)
            current_sum -= A[left]
            left += 1

    print(count)

if __name__ == "__main__":
    main()
