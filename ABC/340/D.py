import sys
import heapq


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))

    def dijkstra(self, start):
        inf = float('inf')
        dist = [inf] * self.n
        dist[start] = 0
        queue = [(0, start)]

        while queue:
            d, u = heapq.heappop(queue)
            if dist[u] < d:
                continue
            for v, w in self.edges[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(queue, (dist[v], v))
        return dist


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = Graph(N)
    for i in range(N - 1):
        a, b, x = map(int, input().split())
        graph.add_edge(i, i + 1, a)  # ステージiからi+1への遷移
        graph.add_edge(i, x-1, b)    # ステージiからxへの遷移、xを0ベースのインデックスに調整

    dist = graph.dijkstra(0)
    print(dist[N - 1])


if __name__ == "__main__":
    main()
