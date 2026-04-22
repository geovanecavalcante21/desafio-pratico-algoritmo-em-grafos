"""LeetCode 133 - Clone Graph

Solução em Python usando DFS.

Observação:
No LeetCode, a classe Node já é fornecida pela plataforma.
O bloco abaixo é mantido para facilitar testes locais.
"""

from __future__ import annotations
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited: Dict[Node, Node] = {}

        def dfs(current: Node) -> Node:
            if current in visited:
                return visited[current]

            clone = Node(current.val)
            visited[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


if __name__ == "__main__":
    # Exemplo simples de teste local:
    # 1 -- 2
    # |    |
    # 4 -- 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = Solution().cloneGraph(n1)
    print("Nó clonado:", cloned.val)
    print("Vizinhos do nó clonado:", [n.val for n in cloned.neighbors])
