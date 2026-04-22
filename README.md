# Desafio Prático: Algoritmos em Grafos — Da Teoria ao Mundo Real

## Integrantes
- [Nome do integrante 1]
- [Nome do integrante 2]
- [Nome do integrante 3]

---

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de **grafos** em dois contextos diferentes:

1. **Ambiente teórico**, por meio da resolução de problemas no LeetCode.
2. **Ambiente real**, por meio do consumo de uma API pública e da aplicação de um algoritmo de grafos sobre dados dinâmicos.

A proposta do trabalho foi mostrar que algoritmos clássicos como **DFS** e **BFS** não servem apenas para exercícios acadêmicos, mas também podem ser reutilizados em situações reais.

---

## Objetivo da atividade

O objetivo deste trabalho foi consolidar o entendimento sobre estruturas de dados em grafos, aplicando algoritmos clássicos tanto em problemas controlados de programação quanto em um cenário real com dados vindos de uma API pública.

---

# Fase 1 — Problemas escolhidos no LeetCode

Foram escolhidos 2 problemas de dificuldade **Medium** relacionados a grafos.

---

## 1. Clone Graph

### Descrição do problema
Neste problema, o objetivo é criar uma **cópia profunda** de um grafo, preservando sua estrutura de conexões, mas sem reutilizar os nós originais.

### Abordagem utilizada
A solução foi implementada com **DFS (Depth-First Search)**.

A lógica utilizada foi:

- verificar se o nó atual já foi clonado;
- usar um dicionário `visited` para relacionar cada nó original ao seu clone;
- percorrer recursivamente os vizinhos do nó atual;
- montar o novo grafo mantendo a mesma estrutura do original.

### Por que essa abordagem funciona
Como o grafo pode ter ciclos, não basta sair copiando os nós recursivamente sem controle. O dicionário `visited` evita duplicação de nós e impede loops infinitos durante a travessia.

### Complexidade
- **Tempo:** `O(V + E)`
- **Espaço:** `O(V)`

Onde:
- `V` = número de vértices
- `E` = número de arestas

---

## 2. Number of Provinces

### Descrição do problema
Neste problema, é dada uma matriz `isConnected`, em que cada posição informa se duas cidades estão conectadas. O objetivo é descobrir quantas **províncias** existem, ou seja, quantos grupos de cidades estão conectados direta ou indiretamente.

### Abordagem utilizada
A solução foi implementada com **DFS (Depth-First Search)**.

A lógica utilizada foi:

- percorrer cada cidade da matriz;
- verificar se ela já foi visitada;
- quando uma cidade não visitada é encontrada, iniciar uma DFS;
- marcar todas as cidades conectadas a ela;
- contar cada nova DFS iniciada como uma nova província.

### Por que essa abordagem funciona
Cada execução de DFS percorre exatamente um componente conectado do grafo. Assim, contar quantas vezes é necessário iniciar uma nova DFS equivale a contar quantas províncias existem.

### Complexidade
- **Tempo:** `O(n²)`
- **Espaço:** `O(n)`

Onde:
- `n` = número de cidades

---

# Fase 2 — Aplicação no mundo real

Na parte prática, foi utilizada a **API pública do GitHub** para construir uma rede de usuários em forma de grafo.

## Problema proposto
Descobrir o **grau de separação** entre dois usuários do GitHub.

Em outras palavras, o objetivo foi verificar em quantos “saltos” é possível sair de um usuário e chegar até outro dentro da rede de conexões.

---

## API escolhida

Foi utilizada a **API pública do GitHub** para consultar informações relacionadas a usuários, seguidores e pessoas seguidas.

---

## Modelagem dos dados em forma de grafo

Os dados foram modelados da seguinte forma:

- **Nós:** usuários do GitHub
- **Arestas:** relações de seguir ou ser seguido

Com isso, a rede de usuários foi tratada como um **grafo social**.

---

## Algoritmo utilizado na aplicação real

Para essa etapa, foi utilizada **BFS (Breadth-First Search)**.

### Motivo da escolha
A BFS é adequada para encontrar o **menor caminho em número de arestas** em grafos não ponderados.

Como o objetivo era descobrir o menor número de conexões entre dois usuários, essa foi a abordagem mais apropriada.

---

## Funcionamento da aplicação

O script:

- recebe um usuário de origem;
- recebe um usuário de destino;
- recebe uma profundidade máxima;
- consulta a API do GitHub;
- recupera os seguidores e usuários seguidos do perfil atual;
- monta a vizinhança do grafo dinamicamente;
- utiliza BFS para buscar um caminho entre os dois usuários.

---

## Resultado obtido no teste

No teste realizado, o programa retornou:

- **Origem:** `torvalds`
- **Destino:** `gaearon`
- **Profundidade máxima:** `3`
- **Grau de separação:** `2`
- **Caminho encontrado:** `torvalds -> antelio -> gaearon`

### Interpretação do resultado
Isso significa que foi encontrado um caminho entre os dois usuários em **2 conexões**, passando por um usuário intermediário.

---

## Complexidade teórica da aplicação real

- **Tempo:** `O(V + E)`
- **Espaço:** `O(V)`

Na prática, o desempenho também depende de fatores externos, como:

- quantidade de conexões de cada usuário;
- tempo de resposta da API;
- limite de requisições.

---

# Estrutura atual do projeto

Atualmente, os arquivos estão organizados assim:

```text
.
├── .gitignore
├── README.md
├── github_degree_separation.py
├── leetcode_clone_graph.py
└── leetcode_number_of_provinces.py
```

---

# Tecnologias utilizadas

- Python
- API pública do GitHub
- Biblioteca `requests`

---

# Como executar o projeto

## 1. Instalar a dependência necessária

No terminal, execute:

```bash
python -m pip install requests
```

Se necessário, também pode ser usado:

```bash
py -m pip install requests
```

---

## 2. Executar o problema Clone Graph

```bash
python .\leetcode_clone_graph.py
```

ou

```bash
py .\leetcode_clone_graph.py
```

### Saída esperada

```text
Nó clonado: 1
Vizinhos do nó clonado: [2, 4]
```

---

## 3. Executar o problema Number of Provinces

```bash
python .\leetcode_number_of_provinces.py
```

ou

```bash
py .\leetcode_number_of_provinces.py
```

### Saída esperada

```text
Número de províncias: 2
```

---

## 4. Executar a aplicação real com a API do GitHub

```bash
python .\github_degree_separation.py torvalds gaearon 3
```

ou

```bash
py .\github_degree_separation.py torvalds gaearon 3
```

### Significado dos parâmetros

- `torvalds` = usuário de origem
- `gaearon` = usuário de destino
- `3` = profundidade máxima da busca

### Exemplo de saída obtida

```text
Origem: torvalds
Destino: gaearon
Profundidade máxima: 3
Grau de separação: 2
Caminho: torvalds -> antelio -> gaearon
```

---

# Demonstração da atividade

A apresentação pode ser organizada em duas partes:

## Parte 1 — Problemas escolhidos no LeetCode

### Problema 1: Clone Graph
- explicar que o objetivo é clonar um grafo;
- mostrar o uso de DFS;
- mostrar o papel do dicionário `visited`;
- comentar a complexidade da solução;
- apresentar o resultado do teste local.

### Problema 2: Number of Provinces
- explicar que o objetivo é contar grupos conectados;
- mostrar o uso de DFS para percorrer cidades conectadas;
- explicar que cada nova DFS representa uma nova província;
- comentar a complexidade da solução;
- apresentar o resultado do teste local.

---

## Parte 2 — Aplicação real

### API escolhida
A API escolhida foi a **API pública do GitHub**.

### Modelagem dos dados
- cada usuário foi tratado como um **nó**;
- cada relação de seguir ou ser seguido foi tratada como uma **aresta**.

### Algoritmo utilizado
Foi utilizada **BFS**, porque o objetivo era encontrar o menor número de conexões entre dois usuários.

### Resultado da execução
No teste feito, foi encontrado o seguinte caminho:

```text
torvalds -> antelio -> gaearon
```

com **grau de separação 2**.

Isso demonstra que o algoritmo conseguiu encontrar uma conexão real entre dois usuários usando dados obtidos da API.

---

# Conclusão

Este projeto permitiu conectar teoria e prática no estudo de grafos.

Na primeira etapa, os algoritmos foram aplicados em problemas clássicos do LeetCode, permitindo reforçar conceitos como travessia em grafos, componentes conectados e cópia de estruturas.

Na segunda etapa, a mesma base algorítmica foi aplicada em dados reais obtidos da API pública do GitHub. Com isso, foi possível demonstrar que algoritmos como **DFS** e **BFS** têm utilidade concreta fora do ambiente acadêmico, sendo aplicáveis à exploração de redes, conexões e caminhos em dados dinâmicos.

---

# Observação final

Os testes mostraram que:

- a cópia do grafo foi realizada corretamente;
- a contagem de províncias funcionou como esperado;
- a aplicação real conseguiu encontrar uma conexão entre dois usuários do GitHub;
- a reutilização de algoritmos clássicos de grafos em um cenário real foi bem-sucedida.
