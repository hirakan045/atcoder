def main() -> None:
    import heapq
    from collections import defaultdict

    def dijkstra(graph, start):
        # 最短距離を保持する辞書
        min_distance = {node: float('inf') for node in graph}
        min_distance[start] = 0

        # 探索する頂点を保持する優先度付きキュー
        priority_queue = [(0, start)]

        while priority_queue:
            # 最小距離の頂点を取り出す
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # 現在の頂点の距離が、記録されてる最短距離よりも大きい場合は処理をしない
            if current_distance > min_distance[current_vertex]:
                continue

            # 隣接する拡張店に対して距離を更新
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                # 記録されている距離より小さい場合は更新
                if distance < min_distance[neighbor]:
                    min_distance[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return min_distance

    N = int(input())

    graph = defaultdict(lambda: defaultdict(int))
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    ans = sorted(dijkstra(graph, 1).items())
    ans = list(map(lambda x: x[1] % 2, ans))
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()