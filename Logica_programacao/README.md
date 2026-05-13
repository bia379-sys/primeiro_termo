# Aula: Lógica de Programação com Python, Boas Práticas e Controle de Versão

## 1. Conteúdo de Aula: Lógica de Programação em Python
Fundamentos essenciais para construir algoritmos estruturados e eficientes.

### 🐍 Variáveis e Tipos de Dados
* Armazenam dados na memória do computador com tipagem dinâmica.
* **Tipos básicos:** `str` (texto), `int` (inteiro), `float` (decimal) e `bool` (booleano).
* **Exemplo:** `idade = 25` ou `nome = "Ana"`.

### 🔀 Estruturas Condicionais
* Desviam o fluxo de execução do código com base em testes lógicos.
* Utiliza as palavras-reservadas `if`, `elif` e `else`.
* **Exemplo:**
  ```python
  if nota >= 7:
      print("Aprovado")
  else:
      print("Reprovado")
  ```

### 🔄 Estruturas de Repetição
* Executam um bloco de código repetidas vezes enquanto uma condição for verdadeira.
* **`while`:** Usado quando não se sabe o número exato de repetições.
* **`for`:** Usado para iterar sobre sequências (listas, intervalos ou textos).
* **Exemplo:**
  ```python
  for i in range(1, 6):
      print(f"Tentativa {i}")
  ```

---

## 2. Controle de Versão: Git e GitHub
Ferramentas indispensáveis para o rastreamento de código e trabalho em equipe.

### 🛠️ Git (Local)
* Sistema de controle de versão distribuído para registrar o histórico de modificações do código.
* **`git init`:** Cria um repositório local novo.
* **`git add .`:** Salva as alterações atuais na área de preparação (*staging area*).
* **`git commit -m "mensagem"`:** Grava as alterações permanentemente no histórico local.

### 🌐 GitHub (Nuvem)
* Plataforma de hospedagem de código na nuvem que integra recursos de colaboração baseados no Git.
* Permite compartilhar projetos, gerenciar tarefas e receber contribuições.
* **`git push`:** Envia as alterações do computador local para o servidor remoto do GitHub.
* **`git pull`:** Baixa as atualizações da nuvem para atualizar o computador local.

---

## 3. Clean Code (Código Limpo)
Práticas de escrita para tornar o código legível, compreensível e fácil de manter.

### 📝 Regras Essenciais para Iniciantes
* **Nomes Significativos:** Variáveis e funções devem revelar sua intenção real (use `total_vendas` em vez de `tv`).
* **Padrão Snake Case:** Em Python, nomes de variáveis e funções devem usar letras minúsculas separadas por sublinhado.
* **Funções Pequenas:** Cada função deve realizar apenas uma tarefa específica muito bem.
* **Evite Comentários Óbvios:** O código limpo deve ser autoexplicativo; comente apenas o "porquê" e nunca o "o quê".
* **Exemplo Prático:**
  ```python
  # Código Ruim
  def calc(x, y):
      return x * y

  # Código Limpo (Clean Code)
  def calcular_area_retangulo(largura, altura):
      return largura * altura
  ```

---

## 4. Projetos Práticos sugeridos para os Alunos
Aplicações reais para fixar os conceitos de lógica, versionamento e organização.

### 🎲 Projeto 1: Jogo de Adivinhação de Números
* **Descrição:** O computador escolhe um número aleatório e o usuário tenta adivinhar com dicas de "maior" ou "menor".
* **Conceitos aplicados:** Condicionais, loops `while`, entrada de dados (`input`) e biblioteca `random`.

### 📋 Projeto 2: Sistema de Cadastro de Tarefas (To-Do List)
* **Descrição:** Terminal interativo para adicionar, listar, marcar como concluída e excluir tarefas cotidianas.
* **Conceitos aplicados:** Listas (`lists`), funções estruturadas, manipulação de strings e Clean Code.
