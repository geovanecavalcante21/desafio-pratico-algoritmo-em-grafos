"""LeetCode 547 - Number of Provinces

Solução em Python usando DFS sobre matriz de adjacência.
"""

from typing import List, Set


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited: Set[int] = set()
        provinces = 0

        def dfs(city: int) -> None:
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces


if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
    print("Número de províncias:", Solution().findCircleNum(matrix))
