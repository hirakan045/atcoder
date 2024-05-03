from collections import deque


def bfs(graph, start_vertex):
    """
    幅優先探索 (Breadth-First Search)

    :param graph: 探索するグラフ（辞書型で隣接リストを表現）
    :param start_vertex: 探索を開始する頂点
    :return: 探索順に並べられた頂点のリスト
    """
    # 探索済みの頂点を保持するセット
    visited = set()
    # 探索する頂点を保持するキュー
    queue = deque([start_vertex])
    # 探索結果を格納するリスト
    order = []

    while queue:
        # キューから頂点を取り出す
        vertex = queue.popleft()
        if vertex not in visited:
            # 未探索の頂点を探索済みとしてマーク
            visited.add(vertex)
            # 探索順に結果リストに追加
            order.append(vertex)
            # 隣接する頂点をキューに追加
            queue.extend(graph[vertex] - visited)

    return order


# グラフの定義（隣接リスト）
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 幅優先探索を開始する頂点
start_vertex = 'A'

# 幅優先探索を実行
order = bfs(graph, start_vertex)
print("探索順:", order)
