# Aula: Engenharia de Requisitos - Técnicas de Levantamento

## 1. Introdução
O levantamento (ou elicitação) de requisitos é a fase do desenvolvimento de software onde se descobrem as necessidades do cliente e dos usuários finais. O objetivo principal é compreender o problema para projetar a solução correta.

---

## 2. Tipos de Requisitos
Os requisitos de um sistema são divididos em três categorias principais:

### 📌 Requisitos Funcionais (RF)
* Definem as funções e comportamentos que o sistema deve executar.
* Representam as ações diretas do usuário ou processos automatizados.
* **Exemplo:** "O sistema deve permitir que o usuário recupere a senha via e-mail."

### ⚡ Requisitos Não-Funcionais (RNF)
* Definem as restrições, qualidades e propriedades globais do sistema.
* Relacionados a desempenho, segurança, usabilidade, confiabilidade e portabilidade.
* **Exemplo:** "O sistema deve criptografar todas as senhas usando a hash SHA-256."

### 💼 Regras de Negócio (RN)
* São premissas, políticas ou restrições da própria organização que o software deve respeitar.
* Não são recursos do sistema, mas leis organizacionais que moldam os requisitos.
* **Exemplo:** "Clientes VIP têm direito a 15% de desconto em compras acima de R$ 200,00."

---

## 3. Principais Técnicas de Levantamento
Escolha a técnica com base no perfil do cliente e no tipo de projeto:

* **Entrevistas:** Conversas diretas (estruturadas ou abertas) com partes interessadas para coletar dados detalhados.
* **Questionários:** Formulários enviados a um grande número de usuários para coletar dados estatísticos rapidamente.
* **Brainstorming:** Reuniões de tempestade de ideias para gerar conceitos inovadores e alinhar expectativas.
* **Workshop de Requisitos:** Sessões intensivas de cocriação com usuários e desenvolvedores trabalhando juntos.
* **Observação Direta (Etnografia):** O analista acompanha o trabalho diário do usuário para entender a rotina real.
* **Prototipagem:** Construção de telas e interfaces rápidas para o usuário validar o fluxo visualmente.

---

## 4. O Processo de Elicitação e Análise
1. **Descoberta:** Identificar as partes interessadas (*stakeholders*) e coletar os dados iniciais.
2. **Classificação:** Organizar os requisitos em funcionais, não-funcionais e regras de negócio.
3. **Priorização:** Negociar com o cliente o que é essencial para o MVP (Mínimo Produto Viável).
4. **Especificação:** Documentar os requisitos detalhadamente (em formato de Histórias de Usuário ou Casos de Uso).
5. **Validação:** Revisar os documentos com o cliente para garantir que não há mal-entendidos.

---

## 5. Boas Práticas e Desafios
* **Falta de Clareza:** Clientes nem sempre sabem expressar o que precisam.
* **Escopo Volátil:** Requisitos mudam constantemente durante o projeto.
* **Linguagem Clara:** Evite termos técnicos complexos ao falar com o cliente final.
* **Rastreabilidade:** Mantenha um histórico de quem solicitou cada funcionalidade e o motivo.
