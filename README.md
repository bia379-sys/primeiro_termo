# primeiro_termo
Material de aula para o 1° termo - LOPAL - SOP - ARI - LER

## LOPAL 
Lógica de programação em Python

## SOP
Sistemas operacionais 

# Resumo Executivo: Do Levantamento de Requisitos à Infraestrutura IoT

Este documento consolida os fundamentos essenciais de quatro pilares da tecnologia: Engenharia de Requisitos, Lógica de Programação, Sistemas Operacionais e Arquitetura de Redes/IoT.

---

## 🗺️ 1. Engenharia de Requisitos: A Concepção do Sistema
O sucesso de qualquer projeto de tecnologia depende da correta identificação e documentação das necessidades do negócio.

### 📌 Classificação de Escopo
* **Requisitos Funcionais (RF):** O que o sistema deve fazer (ex: o app deve alertar quando a temperatura do sensor atingir 40°C).
* **Requisitos Não-Funcionais (RNF):** Como o sistema deve se comportar (ex: o tráfego de dados deve ser criptografado).
* **Regras de Negócio (RN):** Premissas da organização (ex: apenas engenheiros seniores podem alterar os limites de alertas).

### 🛠️ Técnicas de Elicitação
* **Entrevistas:** Alinhamento direto e detalhado com as partes interessadas (*stakeholders*).
* **Brainstorm:** Reuniões dinâmicas voltadas à inovação e geração de ideias livres.
* **Prototipagem:** Modelos visuais das interfaces para validação rápida antes do código.

---

## 🐍 2. Lógica de Programação com Python e Boas Práticas
A tradução dos requisitos em lógica computacional executável e de fácil manutenção.

### 🔤 Fundamentos de Construção
* **Variáveis Dinâmicas:** Armazenamento flexível de tipos de dados (`str`, `int`, `float`, `bool`).
* **Estruturas de Decisão (`if/elif/else`):** Desvios condicionais executados com base em testes lógicos.
* **Laços de Repetição (`for`/`while`):** Automação de tarefas repetitivas e iteração sobre sequências.

### ✨ Princípios de Clean Code (Código Limpo)
* **Nomes Significativos:** Variáveis e funções declaradas de forma autoexplicativa utilizando *snake_case*.
* **Modularização:** Funções pequenas que executam estritamente uma única responsabilidade.
* **Versionamento Profissional:** Rastreamento local via **Git** (`init`, `add`, `commit`) e colaboração em nuvem via **GitHub** (`push`, `pull`).

---

## 🪟 3. Sistemas Operacionais e Operação via CLI
O ambiente onde os sistemas e ferramentas de desenvolvimento rodam e interagem com o hardware.

### 🐧 Windows vs. Linux
* **Windows:** Domínio em estações de trabalho corporativas, gerenciamento visual e uso do Prompt de Comando (CMD).
* **Linux:** Domínio absoluto em servidores de nuvem e sistemas embarcados devido à estabilidade e leveza do Kernel.

### 🖥️ Administração de Sistema via Linha de Comando (CLI)
* **Navegação Básica:** Comandos equivalentes para gerenciamento de diretórios e arquivos (`dir`/`ls`, `mkdir`, `cd`).
* **Gerenciamento Windows Avançado:** Configuração de variáveis de ambiente (`set`/`setx`), controle de usuários (`net user`) e aplicação do Princípio do Menor Privilégio para garantir a **Segurança Cibernética**.

---

## 🌐 4. Arquitetura IoT e Infraestrutura de Redes
A convergência final onde o código gerencia dados físicos enviados do mundo real diretamente para a nuvem.

### 🔀 Estrutura de Conectividade
* **Ativos de Rede:** Equipamentos que processam ou direcionam dados (ex: Roteadores, Switches, Gateways IoT).
* **Passivos de Rede:** Estruturas físicas de suporte para transmissão (ex: Cabos UTP, Patch Panels, Antenas).
* **Derivações da Rede:** Segmentação entre redes restritas (**Intranet**), compartilhadas (**Extranet**) e mundiais (**Internet/IoT**).

### 🤖 Hardware e Protocolos IoT
* **Microcontrolador ESP32:** Dispositivo de borda embarcado de baixo custo com Wi-Fi e Bluetooth nativos (requer drivers como CP2102/CH340 para comunicação serial).
* **Protocolo MQTT:** Protocolo de mensagem extremamente leve baseado no modelo **Publish/Subscribe**, ideal para economizar banda e energia em cenários de internet das coisas através de um **Broker** central.
