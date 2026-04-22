"""Aplicação real com API pública do GitHub.

Objetivo:
Descobrir o grau de separação entre dois usuários usando BFS.

Uso:
    python github_degree_separation.py origem destino [max_depth]

Exemplo:
    python github_degree_separation.py torvalds gaearon 3

Token opcional:
    Defina a variável de ambiente GITHUB_TOKEN para aumentar o limite de requisições.
"""

from __future__ import annotations

import os
import sys
import time
from collections import deque
from typing import Dict, List, Optional, Set, Tuple

import requests

BASE_URL = "https://api.github.com"
TIMEOUT = 15
DEFAULT_MAX_DEPTH = 3
PER_PAGE = 100


class GitHubAPIError(Exception):
    """Erro de acesso à API do GitHub."""


class GitHubGraphExplorer:
    def __init__(self, token: Optional[str] = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "graph-assignment-demo",
        })
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

        self.cache: Dict[Tuple[str, str], List[str]] = {}

    def _get(self, endpoint: str) -> List[dict]:
        url = f"{BASE_URL}{endpoint}"
        response = self.session.get(url, timeout=TIMEOUT)

        if response.status_code == 404:
            raise GitHubAPIError(f"Recurso não encontrado: {url}")

        if response.status_code == 403:
            remaining = response.headers.get("X-RateLimit-Remaining")
            reset = response.headers.get("X-RateLimit-Reset")
            msg = "A requisição foi bloqueada pela API (possível rate limit)."
            if remaining is not None:
                msg += f" Restante: {remaining}."
            if reset is not None:
                msg += f" Reset em unix time: {reset}."
            raise GitHubAPIError(msg)

        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            raise GitHubAPIError("Resposta inesperada da API do GitHub.")
        return data

    def _list_user_relation(self, username: str, relation: str) -> List[str]:
        cache_key = (username.lower(), relation)
        if cache_key in self.cache:
            return self.cache[cache_key]

        if relation not in {"followers", "following"}:
            raise ValueError("relation deve ser 'followers' ou 'following'.")

        endpoint = f"/users/{username}/{relation}?per_page={PER_PAGE}&page=1"
        data = self._get(endpoint)
        users = [item["login"] for item in data if "login" in item]
        self.cache[cache_key] = users
        return users

    def neighbors(self, username: str) -> List[str]:
        followers = self._list_user_relation(username, "followers")
        following = self._list_user_relation(username, "following")
        # Usa set para evitar repetição e trata a rede como explorável por vizinhança social.
        return sorted(set(followers) | set(following))


def bfs_degree_of_separation(
    explorer: GitHubGraphExplorer,
    source: str,
    target: str,
    max_depth: int = DEFAULT_MAX_DEPTH,
    pause_seconds: float = 0.0,
) -> Optional[List[str]]:
    source = source.strip()
    target = target.strip()

    if source.lower() == target.lower():
        return [source]

    queue = deque([(source, [source], 0)])
    visited: Set[str] = {source.lower()}

    while queue:
        current, path, depth = queue.popleft()

        if depth >= max_depth:
            continue

        try:
            neighbors = explorer.neighbors(current)
        except GitHubAPIError as exc:
            print(f"Aviso ao consultar '{current}': {exc}")
            continue

        for neighbor in neighbors:
            key = neighbor.lower()
            if key in visited:
                continue

            new_path = path + [neighbor]
            if key == target.lower():
                return new_path

            visited.add(key)
            queue.append((neighbor, new_path, depth + 1))

        if pause_seconds > 0:
            time.sleep(pause_seconds)

    return None


def main() -> int:
    if len(sys.argv) < 3:
        print("Uso: python github_degree_separation.py origem destino [max_depth]")
        return 1

    source = sys.argv[1]
    target = sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) >= 4 else DEFAULT_MAX_DEPTH

    token = os.getenv("GITHUB_TOKEN")
    explorer = GitHubGraphExplorer(token=token)

    try:
        path = bfs_degree_of_separation(
            explorer=explorer,
            source=source,
            target=target,
            max_depth=max_depth,
            pause_seconds=0.0,
        )
    except requests.RequestException as exc:
        print(f"Erro de rede: {exc}")
        return 1

    print(f"Origem: {source}")
    print(f"Destino: {target}")
    print(f"Profundidade máxima: {max_depth}")

    if path is None:
        print("Resultado: nenhum caminho encontrado dentro do limite informado.")
        return 0

    degree = len(path) - 1
    print(f"Grau de separação: {degree}")
    print("Caminho:", " -> ".join(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
