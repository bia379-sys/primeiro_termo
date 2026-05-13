# Aula: Sistemas Operacionais, Operação via CLI e Segurança Cibernética

## 1. Conteúdo de Aula: Sistemas Operacionais (Windows vs. Linux)
Análise comparativa das duas plataformas mais utilizadas no mercado corporativo e de servidores.

### 🪟 Microsoft Windows
* **Arquitetura:** Baseada no ecossistema comercial e proprietário NT.
* **Características:** Forte apelo visual, compatibilidade em massa com hardwares domésticos e domínio em ambientes de escritório corporativo.
* **Gerenciamento:** Centralizado pelo Active Directory (AD) e Registro do Windows em redes corporativas.

### 🐧 Linux
* **Arquitetura:** Kernel de código aberto (*open-source*), multiprocessado e multiusuário.
* **Características:** Alta estabilidade, modularidade e domínio absoluto em servidores de nuvem, supercomputadores e dispositivos IoT.
* **Distribuições (Distros):** Variações baseadas no mesmo kernel para propósitos específicos (ex: Ubuntu para facilidade, Debian para estabilidade, Alpine para containers).

---

## 2. Operação de S.O. via CLI (Interface de Linha de Comando)
A habilidade de administrar sistemas sem interface gráfica utilizando o terminal.

### 🔤 Comandos Fundamentais de Navegação e Arquivos

| Operação | Windows (CMD) | Linux (Bash) |
| :--- | :--- | :--- |
| Listar conteúdo do diretório | `dir` | `ls -la` |
| Mudar de diretório atual | `cd caminho` | `cd caminho` |
| Exibir pasta atual na tela | `cd` | `pwd` |
| Criar uma pasta nova | `mkdir nome` | `mkdir nome` |
| Copiar arquivos ou diretórios | `copy` ou `xcopy` | `cp` |
| Mover ou renomear arquivos | `move` | `mv` |
| Apagar arquivos permanentemente | `del` | `rm` |

---

## 3. Administração via CLI no Windows (Variáveis, Pastas e Usuários)
Prática de gerenciamento de recursos do sistema através do Prompt de Comando (CMD) administrado.

### ⚙️ Manipulação de Variáveis de Ambiente
* Variáveis guardam dados dinâmicos do sistema (como caminhos de programas).
* **Exibir uma variável existente:** `echo %USERNAME%` ou `echo %PATH%`
* **Criar variável temporária (sessão atual):** `set MINHA_VAR=123`
* **Criar variável permanente no sistema:** `setx NOVO_CAMINHO "C:\Ferramentas"`

### 📂 Gerenciamento de Pastas e Permissões
* **Criar estrutura de pastas em árvore:** `mkdir Projeto\Codigo\Testes`
* **Modificar atributos de arquivos (ocultar/proteger):** `attrib +h +r documento.txt`
* **Controlar permissões de acesso via CLI:** `icacls "C:\PastaRestrita" /grant Usuario:F` *(Concede controle total)*

### 👤 Gerenciamento de Usuários e Grupos
* *Nota: Requer executar o CMD como Administrador.*
* **Listar todos os usuários locais:** `net user`
* **Criar um novo usuário com senha:** `net user AlunoSeguro SenhaForte123 /add`
* **Adicionar usuário ao grupo de Administradores:** `net localgroup Administradores AlunoSeguro /add`
* **Desativar uma conta de usuário:** `net user AlunoSeguro /active:no`

---

## 4. Fundamentos de Segurança Cibernética nos S.O.
Mecanismos práticos para proteger o sistema operacional contra ameaças e acessos não autorizados.

### 🔐 Princípio do Menor Privilégio (PoLP)
* Usuários e processos devem rodar com o nível mínimo de permissão necessário para sua função.
* Evita que códigos maliciosos tomem controle total do sistema caso uma conta comum seja invadida.

### 🛡️ Hardening do Sistema Operacional
Processo de mapear e reduzir a superfície de ataque de um sistema através de configurações estritas:
* **Desativação de Serviços:** Desligar recursos e portas de rede que não estão em uso ativo (ex: desativar SMB antigo).
* **Atualizações de Segurança (Patching):** Aplicar correções de vulnerabilidades críticas kernel/sistema imediatamente.
* **Firewall Host-Based:** Bloquear todo o tráfego de entrada por padrão e permitir apenas conexões estritamente homologadas.
