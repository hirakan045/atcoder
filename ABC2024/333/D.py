from collections import deque, defaultdict

def main() -> None:
    N = int(input())
    graph = defaultdict(set)
    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    def bfs(graph, start):
        T = graph[start]
        max_node = 0

        for t in T:
            visited = set()
            visited.add(1)
            queue = deque([t])
            while queue:
                vertex = queue.popleft()  # キューからノードを取り出す
                if vertex not in visited:
                    visited.add(vertex)

                    # まだ訪問していない隣接ノードをキューに追加
                    queue.extend([node for node in graph[vertex] if node not in visited])

            max_node = max(max_node, len(visited))

        return max_node

    # 幅優先探索を実行
    print(N - bfs(graph, 1) + 1)


if __name__ == "__main__":
    main()