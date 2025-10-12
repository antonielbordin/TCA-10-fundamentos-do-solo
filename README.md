# TCA-10-fundamentos-do-solo
Projetos desenvolvidos dentro da disciplina de Mestrado TCA-10 Fundamentos do Solo

## Modulo 01 - Gênese, morfologia e classificação de solos

### Projeto

#### 🧭 1. Objetivo do Projeto

Criar um mapa interativo que ilustre os processos pedogenéticos (ou seja, os processos de formação e evolução do solo) com foco na gênese — mostrando:

- Como o solo se origina a partir da rocha mãe;
- Quais fatores controlam sua formação;
- Como esses fatores interagem ao longo do tempo para formar diferentes tipos de solo.

#### 🧱 2. Estrutura de Conteúdo do Tema: GÊNESE DO SOLO

🔹 A. Conceito

Gênese do solo = processo natural de formação e evolução do solo a partir do material de origem (rocha ou sedimento), sob influência de fatores ambientais.

🔹 B. Fatores de formação (CLORPT – modelo clássico de Jenny, 1941)

| Fator | O que é | Exemplo de efeito |
| -------------------------------- | ------------------------------------------- | ------------------------------------------------------------ |
| **C**lima | Temperatura e precipitação | Intemperismo químico mais intenso em climas úmidos e quentes |
| **L** (Organismos) | Vegetação, microrganismos, animais, humanos | Matéria orgânica, bioturbação, acidez |
| **R**elevo | Topografia e declividade | Solos mais rasos em encostas, mais profundos em áreas planas |
| **P**arente Material (rocha mãe) | Tipo de rocha/sedimento | Basalto → Latossolo Vermelho; Arenito → Neossolo |
| **T**empo | Idade do solo | Solos mais antigos = mais intemperizados e profundos |

👉 Esses fatores interagem entre si, e o mapa pode mostrar essas relações dinâmicas.

🔹 C. Processos Pedogenéticos (transformações)

1. Adição (adição de materiais)
  Ex: deposição de sedimentos, folhas, matéria orgânica.

2. Perda (remoção de materiais)
  Ex: lixiviação (perda de nutrientes), erosão.

3. Transformação
  Ex: decomposição de matéria orgânica, alteração de minerais.

4. Translocação (movimentação dentro do perfil)
  Ex: migração de argilas, sais ou óxidos para camadas inferiores.

Esses quatro processos ocorrem simultaneamente e moldam a morfologia do solo (horizontes A, B, C...).

#### 🗺️ 3. Como Representar Isso no Mapa Interativo

🎯 Objetivo do mapa

Mostrar como os fatores e processos se conectam na formação do solo.

💡 Ideia de estrutura (em forma de grafo):

```text
Gênese do Solo
├── Fatores de Formação (CLORPT)
│   ├── Clima
│   ├── Organismos
│   ├── Relevo
│   ├── Rocha Mãe
│   └── Tempo
└── Processos Pedogenéticos
    ├── Adição
    ├── Perda
    ├── Transformação
    └── Translocação
```

👉 Cada nó pode ter:

- Breve descrição (em tooltip);
- Imagem ilustrativa (perfil de solo, rocha, vegetação);
- Link ou vídeo curto explicativo.

#### 💻 4. Ferramentas Recomendadas para o Mapa Interativo

🔸 Se quiser algo simples, bonito e rápido:

PyVis (Python)

Permite criar mapas interativos (grafos) em HTML.

Dá pra abrir no navegador e apresentar direto na aula.

📍 Exemplo de nó:

```python
from pyvis.network import Network
net = Network(height="700px", width="100%", bgcolor="#fff")

net.add_node("Gênese do Solo", title="Processo de formação do solo a partir da rocha mãe")
net.add_node("Clima", title="Temperatura e chuva influenciam o intemperismo")
net.add_node("Rocha Mãe", title="Origem mineral do solo")
net.add_node("Tempo", title="Idade do solo")
net.add_edge("Gênese do Solo", "Clima")
net.add_edge("Gênese do Solo", "Rocha Mãe")
net.add_edge("Gênese do Solo", "Tempo")

net.show("genesesolo.html")
```

🔸 Se quiser um mapa com imagens reais e geolocalização:

Folium (Python + Leaflet) → mapa real do Brasil mostrando solos formados por diferentes rochas.

🔸 Se quiser gamificação:

Usar Dash → o aluno clica em um fator (“Clima”) e aparece um mini quiz sobre como ele afeta o solo.

#### 🎤 5. Estrutura da Apresentação Oral

Duração sugerida: 10 a 15 minutos.
Ordem recomendada:

1. Introdução: o que é gênese do solo e por que é importante (1 min).
2. Fatores de formação (CLORPT) – cada integrante pode explicar um fator (5 min).
3. Processos pedogenéticos (adição, perda, transformação, translocação) (3 min).
4. Mapa interativo – demonstração, explicando como os fatores se conectam (4 min).
5. Conclusão: relação entre gênese e sustentabilidade agrícola (1–2 min).

#### 🌾 6. Ideias Criativas (para impressionar a banca/professor)

- Inserir imagens reais de perfis de solo do Paraná (EMBRAPA tem um banco excelente).
- Adicionar ícones coloridos para cada processo (chuva = lixiviação, planta = adição, etc).
- Incluir uma legenda animada mostrando a transição da rocha → solo.
- Fazer uma versão gamificada: clique e descubra o fator.

