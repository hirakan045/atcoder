from collections import defaultdict

def main() -> None:
    N, T = map(int, input().split())

    point = defaultdict(int)
    d = defaultdict(int)
    d[0] = N

    count = 1
    for i in range(T):
        A, B = map(int, input().split())
        before = point[A]
        point[A] += B
        after = point[A]
        d[before] -= 1
        d[after] += 1
        if d[before] == 0:
            count -=1
        if d[after] == 1:
            count += 1
        print(count)

if __name__ == "__main__":
    main()