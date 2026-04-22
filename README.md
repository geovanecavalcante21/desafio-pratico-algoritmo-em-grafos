# Desafio Prático: Algoritmos em Grafos — Da Teoria ao Mundo Real

## Integrantes
- [Preencher com os nomes do grupo]

---

## Visão geral da atividade

Este trabalho foi dividido em duas partes:

1. **Fase 1 — Fundamentação Teórica (LeetCode)**
   - Resolução de 2 problemas médios de grafos.
   - Explicação da lógica e análise de complexidade.

2. **Fase 2 — Aplicação no Mundo Real**
   - Consumo de uma API pública gratuita.
   - Modelagem dos dados como grafo.
   - Aplicação de **BFS** para descobrir o grau de separação entre dois usuários do GitHub.

A ideia central do projeto foi mostrar que algoritmos clássicos de grafos, como **DFS** e **BFS**, não servem apenas para exercícios acadêmicos, mas também podem ser reutilizados em problemas reais envolvendo dados dinâmicos.

---

# Fase 1 — Problemas do LeetCode

## Problema 1 — Clone Graph (LeetCode 133)

### Enunciado resumido
Dado um nó de um grafo não direcionado e conectado, é necessário retornar uma **cópia profunda** (deep copy) desse grafo.

### Ideia da solução
Este problema foi resolvido com **DFS**.

A principal dificuldade está em evitar criar múltiplas cópias do mesmo nó. Para isso, usamos um dicionário (`visited`) que associa cada nó original ao seu clone.

### Passo a passo
1. Se o nó for nulo, retornamos `None`.
2. Se o nó atual já foi copiado antes, retornamos a cópia armazenada.
3. Criamos um novo nó clone com o mesmo valor.
4. Salvamos esse clone no mapa `visited`.
5. Percorremos recursivamente os vizinhos do nó original e clonamos cada um deles.
6. Adicionamos os vizinhos clonados ao nó clone.

### Por que funciona?
O DFS visita o grafo em profundidade e garante que cada nó seja copiado apenas uma vez. O mapa `visited` evita ciclos infinitos e duplicação de nós.

### Complexidade
- **Tempo:** `O(V + E)`
- **Espaço:** `O(V)`

Onde:
- `V` = número de vértices
- `E` = número de arestas

---

## Problema 2 — Number of Provinces (LeetCode 547)

### Enunciado resumido
Dada uma matriz `isConnected`, onde `isConnected[i][j] = 1` indica conexão direta entre cidades `i` e `j`, devemos retornar quantas **províncias** existem, isto é, quantos grupos de cidades estão conectados direta ou indiretamente.

### Ideia da solução
Este problema foi resolvido com **DFS** sobre a matriz de adjacência.

Cada cidade ainda não visitada representa o início de uma nova província. A partir dela, fazemos uma busca para marcar todas as cidades que pertencem ao mesmo grupo conectado.

### Passo a passo
1. Criamos um conjunto `visited` para controlar as cidades já processadas.
2. Percorremos todas as cidades.
3. Quando encontramos uma cidade ainda não visitada, isso significa que encontramos uma nova província.
4. Executamos DFS a partir dessa cidade.
5. O DFS visita todas as cidades conectadas a ela.
6. Incrementamos o contador de províncias.

### Por que funciona?
Cada execução de DFS percorre exatamente um componente conexo do grafo. Assim, contar quantas vezes iniciamos uma nova DFS equivale a contar o número de componentes conexos.

### Complexidade
- **Tempo:** `O(n²)`
- **Espaço:** `O(n)`

Onde:
- `n` = número de cidades

Como o grafo é dado em forma de **matriz de adjacência**, precisamos verificar todas as posições relevantes da linha da cidade atual.

---

# Fase 2 — Aplicação no Mundo Real

## API escolhida
Foi utilizada a **API pública do GitHub**, modelando a rede de usuários como um grafo social.

## Problema real proposto
Descobrir o **grau de separação** entre dois usuários do GitHub.

Exemplo de pergunta:
> Em quantos “pulos” é possível chegar de um desenvolvedor a outro dentro da rede de seguidores/seguidos?

---

## Modelagem do grafo

### Nós
Cada usuário do GitHub representa um **nó** do grafo.

### Arestas
Foi considerada uma ligação entre dois usuários quando existe relação pública de **seguir** ou **ser seguido**.

Na prática, ao expandir um usuário durante a busca, coletamos:
- usuários que ele segue;
- usuários que o seguem.

Assim, trabalhamos com um grafo social explorável por vizinhança.

---

## Algoritmo utilizado
Foi utilizada **Busca em Largura (BFS)**.

### Por que BFS?
Porque a BFS é o algoritmo clássico para encontrar o **menor número de arestas** entre um nó de origem e um nó de destino em grafos não ponderados.

Isso combina diretamente com a ideia de grau de separação:
- 1 salto = conexão direta;
- 2 saltos = precisa passar por 1 intermediário;
- 3 saltos = precisa passar por 2 intermediários;
- e assim por diante.

---

## Relação entre a Fase 1 e a Fase 2

O mesmo raciocínio usado no problema **Number of Provinces** foi reaproveitado aqui:

- controlar vértices visitados;
- percorrer vizinhos de cada nó;
- explorar a conectividade do grafo;
- evitar revisitas e ciclos.

A diferença é que, na aplicação real:
- os dados não vêm prontos em memória;
- eles precisam ser obtidos via API;
- o grafo é construído dinamicamente durante a execução.

---

## Funcionamento da aplicação real

O script recebe:
- um usuário de origem;
- um usuário de destino;
- profundidade máxima de busca.

Depois:
1. consulta a API do GitHub;
2. recupera seguidores e seguidos do usuário atual;
3. usa BFS para expandir a rede nível por nível;
4. para quando encontra o destino;
5. retorna o número de saltos e o caminho encontrado.

---

## Complexidade da aplicação real

### Em termos de grafo
Se chamarmos de:
- `V` = usuários efetivamente visitados
- `E` = relações exploradas

A BFS continua tendo custo teórico de:
- **Tempo:** `O(V + E)`
- **Espaço:** `O(V)`

### Na prática
O tempo real também depende de:
- latência da rede;
- limite de requisições da API;
- quantidade de seguidores/seguidos por usuário.

Ou seja, embora a estrutura algorítmica seja eficiente, a aplicação real traz restrições externas que não aparecem em problemas fechados de plataforma.

---

## Resultado esperado
A aplicação informa:
- se existe caminho entre os dois usuários dentro do limite definido;
- qual foi o caminho encontrado;
- quantos saltos foram necessários.

Exemplo de saída:

```text
Origem: userA
Destino: userB
Grau de separação: 3
Caminho: userA -> userX -> userY -> userB
```

---

# Estrutura do repositório

```text
.
├── README.md
├── leetcode_clone_graph.py
├── leetcode_number_of_provinces.py
├── github_degree_separation.py
└── roteiro_apresentacao.md
```

---

# Como executar

## 1. Instalar dependências

```bash
pip install requests
```

## 2. Executar a aplicação real

```bash
python github_degree_separation.py torvalds gaearon 3
```

### Com token opcional do GitHub
Para evitar limitações muito rápidas da API, também é possível usar um token pessoal:

```bash
# Linux/macOS
export GITHUB_TOKEN=seu_token
python github_degree_separation.py torvalds gaearon 3
```

```powershell
# Windows PowerShell
$env:GITHUB_TOKEN="seu_token"
python github_degree_separation.py torvalds gaearon 3
```

---

# Conclusão

Este trabalho mostrou que algoritmos de grafos estudados em ambientes de treino, como LeetCode, podem ser adaptados para resolver problemas concretos. Na Fase 1, utilizamos DFS para manipular conectividade e estruturas de grafo. Na Fase 2, aplicamos BFS em dados reais do GitHub para medir o grau de separação entre desenvolvedores.

Com isso, foi possível conectar teoria e prática, demonstrando que estruturas de dados e algoritmos não são apenas conceitos abstratos, mas ferramentas úteis para interpretar e explorar redes reais.
