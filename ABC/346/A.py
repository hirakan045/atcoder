def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))

    B = []
    for i in range(N-1):
        B.append(str(A[i]*A[i+1]))

    print(" ".join(B))



if __name__ == "__main__":
    main()