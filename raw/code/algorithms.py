"""
Graph Algorithms Implementation
常用图算法的 Python 实现

展示：
- 数据结构设计
- 算法实现
- 复杂度优化
- 测试用例

Author: Demo Code
Created: 2026-04-08
"""

from typing import List, Dict, Set, Tuple, Optional, Callable
from collections import deque, defaultdict
import heapq
from dataclasses import dataclass, field
from enum import Enum


class TraversalStrategy(Enum):
    """图遍历策略"""
    BFS = "breadth_first"  # 广度优先
    DFS = "depth_first"    # 深度优先
    DIJKSTRA = "dijkstra"  # 最短路径


@dataclass
class GraphNode:
    """
    图节点

    WHY: 使用 dataclass 而不是普通字典
    提供类型安全和更好的 IDE 支持
    """
    id: str
    value: any = None
    metadata: Dict = field(default_factory=dict)

    def __hash__(self):
        # IMPORTANT: 实现哈希以支持集合操作
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, GraphNode):
            return False
        return self.id == other.id


@dataclass
class GraphEdge:
    """
    图边
    """
    source: GraphNode
    target: GraphNode
    weight: float = 1.0
    directed: bool = False
    metadata: Dict = field(default_factory=dict)


class Graph:
    """
    图数据结构

    支持有向图和无向图
    使用邻接表实现以优化空间复杂度
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: Dict[str, GraphNode] = {}
        self.edges: Dict[str, Set[GraphEdge]] = defaultdict(set)

        # NOTE: 使用 defaultdict 避免 key 检查
        self.adjacency: Dict[str, Dict[str, float]] = defaultdict(dict)

    def add_node(self, node: GraphNode) -> None:
        """添加节点"""
        if node.id not in self.nodes:
            self.nodes[node.id] = node

    def add_edge(self, edge: GraphEdge) -> None:
        """
        添加边

        WHY: 分离边的创建和添加逻辑
        允许在添加前进行验证
        """
        # 确保节点存在
        self.add_node(edge.source)
        self.add_node(edge.target)

        # 添加边
        self.edges[edge.source.id].add(edge)
        self.adjacency[edge.source.id][edge.target.id] = edge.weight

        # 如果是无向图，添加反向边
        if not edge.directed and not self.directed:
            reverse_edge = GraphEdge(
                source=edge.target,
                target=edge.source,
                weight=edge.weight,
                directed=False
            )
            self.edges[edge.target.id].add(reverse_edge)
            self.adjacency[edge.target.id][edge.source.id] = edge.weight

    def get_neighbors(self, node_id: str) -> List[Tuple[str, float]]:
        """获取节点的邻居"""
        return [
            (neighbor, weight)
            for neighbor, weight in self.adjacency[node_id].items()
        ]

    def __len__(self) -> int:
        return len(self.nodes)

    def __contains__(self, node_id: str) -> bool:
        return node_id in self.nodes


class PathFinder:
    """
    路径查找器

    封装多种路径查找算法
    类似于 Graphify 中的路径查找功能
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def bfs(self, start: str, end: str) -> Optional[List[str]]:
        """
        广度优先搜索 - 最短路径（无权图）

        Time Complexity: O(V + E)
        Space Complexity: O(V)

        WHY: BFS 保证在无权图中找到最短路径
        """
        if start not in self.graph or end not in self.graph:
            return None

        # 队列存储 (当前节点, 路径)
        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path

            # 遍历邻居
            for neighbor, _ in self.graph.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

        return None

    def dfs(self, start: str, end: str) -> Optional[List[str]]:
        """
        深度优先搜索 - 任意路径

        Time Complexity: O(V + E)
        Space Complexity: O(V) - 递归栈

        NOTE: DFS 不保证找到最短路径
        但可能更快找到一条路径
        """
        if start not in self.graph or end not in self.graph:
            return None

        visited = set()

        def dfs_helper(current: str, path: List[str]) -> Optional[List[str]]:
            if current == end:
                return path

            visited.add(current)

            for neighbor, _ in self.graph.get_neighbors(current):
                if neighbor not in visited:
                    result = dfs_helper(neighbor, path + [neighbor])
                    if result:
                        return result

            return None

        return dfs_helper(start, [start])

    def dijkstra(self, start: str, end: str) -> Optional[Tuple[List[str], float]]:
        """
        Dijkstra 算法 - 最短路径（带权图）

        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)

        IMPORTANT: 只适用于非负权重的图
        对于负权重，应该使用 Bellman-Ford 算法
        """
        if start not in self.graph or end not in self.graph:
            return None

        # 优先队列: (距离, 节点, 路径)
        pq = [(0, start, [start])]
        distances = {start: 0}

        while pq:
            current_dist, current, path = heapq.heappop(pq)

            # 如果找到终点
            if current == end:
                return (path, current_dist)

            # 如果已经找到更短的路径
            if current_dist > distances.get(current, float('inf')):
                continue

            # 遍历邻居
            for neighbor, weight in self.graph.get_neighbors(current):
                distance = current_dist + weight

                # 如果找到更短的路径
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (distance, neighbor, new_path))

        return None

    def find_all_paths(
        self,
        start: str,
        end: str,
        max_length: Optional[int] = None
    ) -> List[List[str]]:
        """
        查找所有路径

        HACK: 使用 DFS 但收集所有路径而不是返回第一个
        """
        all_paths = []
        visited = set()

        def find_paths_helper(current: str, path: List[str]) -> None:
            if current == end:
                all_paths.append(path)
                return

            # 检查路径长度限制
            if max_length and len(path) >= max_length:
                return

            visited.add(current)

            for neighbor, _ in self.graph.get_neighbors(current):
                if neighbor not in visited:
                    find_paths_helper(neighbor, path + [neighbor])

            visited.remove(current)

        find_paths_helper(start, [start])
        return all_paths


class CommunityDetector:
    """
    社区检测器

    使用简单的标签传播算法
    类似于 Graphify 中使用的 Leiden 算法
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def label_propagation(
        self,
        max_iterations: int = 100
    ) -> Dict[str, int]:
        """
        标签传播算法

        Time Complexity: O(k * E) where k 是迭代次数
        Space Complexity: O(V)

        NOTE: 这是一个简化版本
        真实的 Leiden 算法更复杂但效果更好
        """
        # 初始化：每个节点有自己的标签
        labels = {node_id: i for i, node_id in enumerate(self.graph.nodes)}

        for _ in range(max_iterations):
            changes = 0

            # 遍历所有节点
            for node_id in self.graph.nodes:
                # 获取邻居的标签频率
                label_counts = defaultdict(int)
                for neighbor, _ in self.graph.get_neighbors(node_id):
                    label_counts[labels[neighbor]] += 1

                if not label_counts:
                    continue

                # 选择最常见的标签
                new_label = max(label_counts.items(), key=lambda x: x[1])[0]

                if labels[node_id] != new_label:
                    labels[node_id] = new_label
                    changes += 1

            # 如果没有变化，收敛
            if changes == 0:
                break

        return labels

    def get_communities(self, labels: Dict[str, int]) -> Dict[int, List[str]]:
        """将标签转换为社区"""
        communities = defaultdict(list)
        for node_id, label in labels.items():
            communities[label].append(node_id)
        return dict(communities)


# ============ 工具函数 ============

def create_sample_graph() -> Graph:
    """创建示例图用于测试"""
    graph = Graph(directed=False)

    # 创建节点
    nodes = [
        GraphNode("A", value="Node A"),
        GraphNode("B", value="Node B"),
        GraphNode("C", value="Node C"),
        GraphNode("D", value="Node D"),
        GraphNode("E", value="Node E"),
    ]

    # 添加边
    edges = [
        GraphEdge(nodes[0], nodes[1]),  # A - B
        GraphEdge(nodes[0], nodes[2]),  # A - C
        GraphEdge(nodes[1], nodes[2]),  # B - C
        GraphEdge(nodes[1], nodes[3]),  # B - D
        GraphEdge(nodes[2], nodes[3]),  # C - D
        GraphEdge(nodes[3], nodes[4]),  # D - E
    ]

    for node in nodes:
        graph.add_node(node)

    for edge in edges:
        graph.add_edge(edge)

    return graph


def main():
    """主函数 - 演示算法使用"""
    print("=== Graph Algorithms Demo ===\n")

    # 创建图
    graph = create_sample_graph()
    print(f"Graph: {len(graph)} nodes, {sum(len(e) for e in graph.edges.values())} edges\n")

    # 路径查找
    finder = PathFinder(graph)

    # BFS
    bfs_path = finder.bfs("A", "E")
    print(f"BFS Path (A → E): {bfs_path}")

    # DFS
    dfs_path = finder.dfs("A", "E")
    print(f"DFS Path (A → E): {dfs_path}")

    # Dijkstra
    dijkstra_result = finder.dijkstra("A", "E")
    if dijkstra_result:
        path, dist = dijkstra_result
        print(f"Dijkstra Path (A → E): {path}, Distance: {dist}")

    # 所有路径
    all_paths = finder.find_all_paths("A", "E")
    print(f"\nAll paths from A to E: {len(all_paths)}")
    for i, path in enumerate(all_paths, 1):
        print(f"  {i}. {' → '.join(path)}")

    # 社区检测
    print("\n=== Community Detection ===")
    detector = CommunityDetector(graph)
    labels = detector.label_propagation()
    communities = detector.get_communities(labels)

    print(f"\nFound {len(communities)} communities:")
    for i, (label, members) in enumerate(communities.items(), 1):
        print(f"  Community {i}: {', '.join(members)}")


if __name__ == '__main__':
    main()
