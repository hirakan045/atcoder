def main() -> None:
    from collections import deque

    T = input()
    N = int(input())

    ans = []
    for i in range(N):
        I = input().split()
        A = I[0]
        S = I[1:]
        for index, element in enumerate(S):
            if i == 0:
                if T.startswith(element):
                    ans.append([str(index), element])

if __name__ == "__main__":
    main()