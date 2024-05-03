def main() -> None:
    N, K = map(int, input().split())
    S = input()

    s1 = S[:K-1]
    s2 = S[K-1].lower()
    s3 = S[K:]

    print(''.join([s1, s2, s3]))

if __name__ == "__main__":
    main()