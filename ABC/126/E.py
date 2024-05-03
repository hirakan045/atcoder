def main() -> None:

    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))  # 各要素の親を指す配列
            self.rank = [0] * size  # 各要素のランク（木の高さ）

        def find(self, p):
            if self.parent[p] != p:
                self.parent[p] = self.find(self.parent[p])  # パス圧縮
            return self.parent[p]

        def union(self, p, q):
            rootP = self.find(p)
            rootQ = self.find(q)
            if rootP != rootQ:
                if self.rank[rootP] > self.rank[rootQ]:
                    self.parent[rootQ] = rootP
                elif self.rank[rootP] < self.rank[rootQ]:
                    self.parent[rootP] = rootQ
                else:
                    self.parent[rootQ] = rootP
                    self.rank[rootP] += 1

        def connected(self, p, q):
            return self.find(p) == self.find(q)

    N, M = map(int, input().split())

    uf = UnionFind(N)

    for i in range(M):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        uf.union(x, y)

    print(len(set(uf.find(i) for i in range(N))))


if __name__ == "__main__":
    main()