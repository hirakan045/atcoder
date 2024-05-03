import math

def main() -> None:
    N = int(input())
    maxN = 10 ** 6

    for i in range(maxN):
        if i ** 3 > N:
            break
        N1 = list(str(i**3))
        N2 = reversed(N1)
        if all(x == y for x, y in zip(N1, N2)):
            ans = "".join(N1)

    print(ans)



if __name__ == "__main__":
    main()