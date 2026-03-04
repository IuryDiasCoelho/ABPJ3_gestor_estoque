# 📦 Gestor de Estoque em Python

Sistema de gerenciamento de estoque desenvolvido em Python para controle de produtos, vendas e valor acumulado em caixa.

Projeto acadêmico – Engenharia de Software.

---

# 📌 Visão Geral

O sistema permite:

- ✔ Cadastrar produtos
- ✔ Atualizar estoque
- ✔ Registrar vendas
- ✔ Listar produtos disponíveis
- ✔ Controlar valor total em caixa
- ✔ Navegação via menu interativo (terminal)

---

# 🏗 Arquitetura do Projeto

```
ABPJ3_gestor_estoque/
│
├── main.py        → Controle principal (menu e fluxo)
├── modulo.py      → Funções do sistema
└── README.md
```

---

# 🧠 Estrutura de Dados

O sistema utiliza dicionários para armazenar as informações:

```python
estoque = { produto: quantidade }
financeiro = { produto: valor_unitario }
caixa = float
```

### 📦 estoque
Armazena o nome do produto e sua quantidade disponível.

### 💰 financeiro
Armazena o valor unitário de cada produto.

### 🏦 caixa
Armazena o total acumulado das vendas realizadas.

---

# 🔄 Fluxo do Sistema

## 📊 Fluxograma Lógico

```
Início
   ↓
Mostrar Menu
   ↓
Usuário escolhe opção
   ↓
┌───────────────────────────────┐
│ 1 - Cadastrar Produto         │
│ 2 - Atualizar Estoque         │
│ 3 - Registrar Venda           │
│ 4 - Estoque Disponível        │
│ 5 - Valor em Caixa            │
│ 6 - Sair                      │
└───────────────────────────────┘
   ↓
Executa ação escolhida
   ↓
Retorna ao Menu (loop while True)
```

---

# 🧾 Funcionalidades Detalhadas

## 1️⃣ Cadastrar Produto

- Solicita:
  - Nome
  - Quantidade
  - Valor unitário
- Armazena nos dicionários:
  - `estoque`
  - `financeiro`

---

## 2️⃣ Atualizar Estoque

- Mostra estoque atual
- Permite cadastrar novamente o produto com nova quantidade
- Atualiza os dicionários

---

## 3️⃣ Registrar Venda

Fluxo interno:

```
Mostrar estoque
↓
Solicitar produto
↓
Verificar se existe
↓
Solicitar quantidade
↓
Verificar se há estoque suficiente
↓
Diminuir estoque
↓
Calcular total da venda
↓
Atualizar caixa
↓
Exibir estoque atualizado
```

Regras:
- Não permite quantidade negativa
- Não permite vender mais do que disponível

---

## 4️⃣ Estoque Disponível

Percorre o dicionário `estoque` e exibe:

```
Produto - Quantidade - Valor
```

---

## 5️⃣ Valor em Caixa

Exibe o valor acumulado:

```
Valor em caixa: R$ X.XX
```

---

# ▶️ Como Executar

## ✅ Requisitos

- Python 3.10 ou superior

## 🚀 Execução

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

---

# 💡 Conceitos Aplicados

- Modularização de código
- Estruturas condicionais (`match-case`)
- Estruturas de repetição (`while`)
- Dicionários
- Manipulação de entrada de usuário
- Tratamento de exceção (`try/except`)
- Escopo de variáveis
- Uso de `global` corretamente
- Separação entre arquivo principal e módulo

---

# 🛠 Tecnologias Utilizadas

- Python 3
- Programação estruturada

---

# 📈 Possíveis Melhorias Futuras

- Persistência de dados com JSON
- Integração com PostgreSQL
- Interface gráfica (Tkinter)
- Versão orientada a objetos
- Sistema de relatórios
- Sistema de login
- Controle de múltiplos usuários
- Deploy como aplicação web

---

# 🎓 Aprendizados Técnicos

Durante o desenvolvimento foram trabalhados conceitos importantes como:

- Importação de módulos
- Problemas com importação circular
- Diferença entre:
  - `from modulo import *`
  - `import modulo`
- Manipulação de variáveis globais
- Organização de projeto Python

---

# 👨‍💻 Autor

**Iury Dias Coelho .**  
Estudante de Engenharia de Software e Desenvolvimento Web e Mobile

Projeto acadêmico para prática de lógica e organização modular em Python.

---

# 📄 Licença

Uso educacional.