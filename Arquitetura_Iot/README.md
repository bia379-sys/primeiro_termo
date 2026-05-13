# Aula: Arquitetura de Soluções IoT e Infraestrutura de Redes

## 1. Conteúdo de Aula: Arquiteturas IoT (Internet das Coisas)
A base para compreender como bilhões de dispositivos inteligentes se conectam, processam dados e interagem com a nuvem.

### 🏛️ Modelo de Arquitetura em Três Camadas
* **Camada de Percepção (Borda/Edge):** Sensores e atuadores que coletam dados do mundo físico e executam ações (ex: ESP32, sensores de temperatura).
* **Camada de Rede (Transmissão):** Infraestrutura que transporta os dados coletados de forma segura até os servidores (ex: Gateways, Wi-Fi, LoRaWAN).
* **Camada de Aplicação (Nuvem/Cloud):** Sistemas que processam, armazenam e exibem as informações para o usuário final (ex: Dashboards, AWS IoT, Azure IoT).

---

## 2. Infraestrutura: Ativos e Passivos de Rede
Componentes físicos que sustentam o tráfego de dados gerado pelos dispositivos IoT.

### ⚡ Ativos de Rede
* Dispositivos eletrônicos que geram, processam, direcionam ou amplificam sinais digitais na rede.
* **Exemplos:**
  * **Roteadores:** Direcionam pacotes de dados entre redes diferentes (ex: da rede local para a nuvem).
  * **Switches:** Conectam vários dispositivos dentro da mesma rede local de forma inteligente.
  * **Gateways IoT:** Traduzem protocolos locais de baixa potência (como Zigbee) para protocolos de internet (como TCP/IP).

### 🔌 Passivos de Rede
* Elementos estruturais que não processam dados, mas servem como meio físico para a transmissão do sinal.
* **Exemplos:**
  * **Cabos de Par Trançado (UTP):** Meio de transmissão físico para redes cabeadas (Ethernet).
  * **Patch Panels:** Painéis organizadores para a distribuição de cabos de rede em racks.
  * **Antenas:** Estruturas físicas passivas que propagam e captam ondas de rádio (Wi-Fi, Bluetooth).

---

## 3. Internet e Suas Derivações
A evolução das redes de comunicação para atender diferentes cenários de conectividade.

* **Intranet:** Rede local restrita de uma organização, inacessível para usuários externos não autorizados.
* **Extranet:** Extensão segura da intranet que permite o acesso externo controlado para parceiros ou fornecedores.
* **Internet:** A rede mundial de computadores pública e interconectada baseada no conjunto de protocolos TCP/IP.
* **IoT (Internet das Coisas):** Extensão da internet que conecta objetos cotidianos, máquinas e sensores à rede para troca autônoma de dados.

---

## 4. Prática Hardware: Driver e Preparação do ESP32
O microcontrolador ESP32 é um dos chips mais populares para prototipagem IoT devido ao seu Wi-Fi e Bluetooth integrados.

### 🛠️ Instalação do Driver USB
* O chip de comunicação serial mais comum no ESP32 é o **CP2102** ou o **CH340**.
* **Passo a passo no ecossistema de desenvolvimento:**
  1. Baixar e instalar o driver correspondente ao chip serial do seu hardware.
  2. Conectar o ESP32 ao computador via cabo USB (certificado para dados, não apenas carregamento).
  3. Verificar no Gerenciador de Dispositivos (Windows) ou terminal (Linux/Mac) qual porta COM/TTY foi associada.

### 💻 Preparação na IDE (Ex: Arduino IDE)
* Adicionar a URL das placas ESP32 nas preferências da IDE.
* Instalar o pacote de placas `esp32` pelo Gerenciador de Placas.
* Selecionar o modelo correto (ex: *ESP32 Dev Module*) e a porta COM identificada para habilitar o upload do código.

---

## 5. Protocolo MQTT e Aplicação em IoT
O MQTT (*Message Queuing Telemetry Transport*) é o protocolo padrão para comunicação IoT devido à sua leveza.

### 📝 Características Principais
* Baseado no modelo **Publish/Subscribe** (Publicação/Assinatura) em vez do tradicional Request/Response (HTTP).
* Roda sobre a pilha TCP/IP, consumindo o mínimo de largura de banda e bateria dos dispositivos de borda.

### 🔄 Arquitetura de Comunicação MQTT
* **Broker:** O servidor central intermediário responsável por receber e repassar as mensagens (ex: Mosquitto, HiveMQ).
* **Publisher:** O dispositivo que envia dados para um canal específico chamado **Tópico** (ex: ESP32 publica a temperatura no tópico `casa/sala/temperatura`).
* **Subscriber:** O dispositivo ou sistema que assina o tópico para receber as atualizações em tempo real (ex: Um app de celular ou sistema na nuvem).

---

## 6. Artefato Técnico: Estrutura de Relatório Técnico IoT
Roteiro para orientar os alunos na documentação de projetos ou laboratórios práticos.

```text
1. CAPA E IDENTIFICAÇÃO (Nome dos alunos, data, título do projeto)
2. OBJETIVO (O que o sistema IoT desenvolvido resolve)
3. ARQUITETURA ESQUEMÁTICA (Desenho ou diagrama unifilar das camadas e conexões)
4. COMPONENTES UTILIZADOS (Lista de hardware ativos/passivos e softwares/brokers)
5. ESQUEMA DE LIGAÇÃO E PROTOCOLO (Descrição dos pinos e tópicos MQTT configurados)
6. CÓDIGO-FONTE COMENTADO (Trechos principais de conexão Wi-Fi e publicação)
7. CONCLUSÃO E TESTES (Resultados medidos e limitações encontradas)
```
