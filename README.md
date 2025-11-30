# Projeto FCCPD – Desafios com Docker, Microsserviços e Gateway

Trabalho prático da segunda unidade da disciplina de **Fundamentos da Computação Concorrente, Paralela e Distribuída (FCCPD)**, composto por cinco desafios independentes, focados em:

- Criação e comunicação entre containers Docker
- Uso de redes bridge personalizadas
- Persistência de dados com volumes
- Orquestração com Docker Compose
- Arquitetura de microsserviços e uso de API Gateway (Nginx)

Cada desafio possui sua própria pasta (`desafio1` a `desafio5`) com arquivos de configuração específicos.

---

# Desafio 1: Containers em Rede

Este desafio implementa dois containers que se comunicam por meio de uma **rede Docker do tipo bridge** criada especificamente para eles. Um container atua como servidor HTTP (Nginx) e o outro como cliente, que faz requisições periódicas para o servidor. A criação dos serviços e da rede é feita com Docker Compose.

---

### INSTRUÇÕES DE EXECUÇÃO

**Pré-requisitos**: Docker e Docker Compose instalados.

1. Entre no diretório do desafio:

```bash
cd desafio1
```

2. Suba os serviços:

```bash
docker compose up
```

3. Observe, no próprio terminal, os logs sendo emitidos em tempo real:

<img width="993" height="260" alt="image" src="https://github.com/user-attachments/assets/7b7f530e-63f7-4ed2-9544-5440867738d9" />


- O container cliente exibirá mensagens informando que está enviando chamadas HTTP.
- O container servidor registrará as requisições recebidas na porta `8080` e responderá com uma mensagem de texto simples.


---

### ARQUITETURA

**Rede:**  
Uma rede do tipo `bridge` chamada `net-desafio1` conecta exclusivamente os dois serviços.

**Container 1 – Servidor (`web_server_d1`)**  
Imagem `nginx:alpine`, configurado via `nginx.conf` customizado, escutando na porta 8080.

**Container 2 – Cliente (`requester_d1`)**  
Imagem `alpine/curl`, executa um loop infinito chamando o servidor a cada alguns segundos.

---

### DECISÕES TÉCNICAS

- Uso de Docker Compose para criação simultânea de rede e containers.
- Resolução de DNS interno usando o nome do serviço.
- Uso de imagens Alpine para leveza.

---

# Desafio 2: Volumes e Persistência de Dados

Este desafio demonstra a persistência de dados utilizando **volumes nomeados** do Docker em um banco PostgreSQL. Um segundo container é usado como “leitor” para acessar os dados via rede.

---

### INSTRUÇÕES DE EXECUÇÃO

```bash
cd desafio2
docker compose up -d
```

Criando dados:

```bash
docker exec -it desafio2-db-container psql -U admin -d desafio2
```

```sql
CREATE TABLE teste_persistencia (
    id SERIAL PRIMARY KEY,
    nome TEXT
);

INSERT INTO teste_persistencia (nome)
VALUES ('registro 1'), ('registro 2');

SELECT * FROM teste_persistencia;
\q
```

<img width="1216" height="688" alt="image" src="https://github.com/user-attachments/assets/fa1b51a1-b909-4d80-a403-3af81a0a4423" />


Testando persistência:

```bash
docker compose down
docker compose up -d
docker exec -it desafio2-db-container psql -U admin -d desafio2 -c "SELECT * FROM teste_persistencia;"
```
<img width="1295" height="186" alt="image" src="https://github.com/user-attachments/assets/2da59ef5-71ca-400c-8b26-1b33c40b3136" />


---

### ARQUITETURA

- Rede `desafio2_network`
- Volume nomeado `desafio2_data_volume`
- Container PostgreSQL principal + container leitor compartilhando volume

---

### DECISÕES TÉCNICAS

- Persistência garantida por volumes nomeados.
- Separação entre banco e container leitor simula cliente externo.
- Imagem `postgres:15-alpine` pela leveza.

---

# Desafio 3: Docker Compose Orquestrando Serviços

Três serviços são configurados via Docker Compose: banco Postgres, cache Redis e um container web usado como ambiente de testes para verificar a comunicação entre os serviços.

---

### INSTRUÇÕES DE EXECUÇÃO

```bash
cd desafio3
docker compose up -d
```

Testando postgres:

```bash
docker exec -it desafio3-database sh
```

Dentro dele:

```bash
psql -U desafio_user -d desafio3_app_db -c '\l'
exit
```

<img width="1216" height="314" alt="image" src="https://github.com/user-attachments/assets/d6bf8aa0-d7da-4d8c-82bd-e72984053542" />


Testando Redis:

```bash
docker exec -it desafio3-cache-service sh
```

Dentro dele:

```bash
redis-cli ping
exit
```

<img width="1082" height="66" alt="image" src="https://github.com/user-attachments/assets/c4814ace-4dab-421c-af5a-35d026bff8ba" />


---

### ARQUITETURA

- Rede `desafio3_network`
- Containers:
  - Banco (`desafio3_database`)
  - Cache (`desafio3_cache`)
  - Web (`desafio3_web`)

---

### DECISÕES TÉCNICAS

- `depends_on` usado para garantir ordem de inicialização.
- Hostnames internos usados para conectar serviços.
- `busybox` como ambiente mínimo para testes.

---

# Desafio 4: Microsserviços Independentes

Dois microsserviços em Flask:  
- Serviço A expõe usuários  
- Serviço B consome o Serviço A e retorna respostas formatadas

---

### INSTRUÇÕES DE EXECUÇÃO

```bash
cd desafio4
docker compose up --build -d
```

Serviço A:

```bash
curl http://localhost:5000/usuarios
```

Serviço B:

```bash
curl http://localhost:5001/info
```

<img width="1304" height="152" alt="image" src="https://github.com/user-attachments/assets/12fd9368-d44d-49fc-80bd-54f980513b48" />


---

### ARQUITETURA

- Rede `desafio4_network`
- Serviço A: Flask em `/usuarios`
- Serviço B: Flask em `/info` consumindo Serviço A via `requests`

---

### DECISÕES TÉCNICAS

- Containerização independente com Dockerfiles distintos.
- Comunicação via HTTP puro.
- URL do Serviço A configurada por variável de ambiente (`SERVICE_A_URL`).

---

# Desafio 5: Microsserviços com API Gateway

O tráfego interno entre microsserviços passa por um **gateway Nginx**, que é o único ponto exposto externamente.

---

### INSTRUÇÕES DE EXECUÇÃO

```bash
cd desafio5
docker compose up --build -d
```

Testando endpoints:

```bash
curl http://localhost/users
curl http://localhost/orders
```

<img width="1465" height="135" alt="image" src="https://github.com/user-attachments/assets/26474680-67f6-47fb-8e55-0940157e42dc" />


---

### ARQUITETURA

- Rede `desafio5_network`
- Gateway Nginx roteando:
  - `/users` → serviço de usuários
  - `/orders` → serviço de pedidos
- Microsserviços Flask rodando internamente (portas não expostas no host)

---

### DECISÕES TÉCNICAS

- Nginx como proxy reverso/API Gateway.
- Microsserviços totalmente isolados do host.
- Roteamento por caminhos HTTP.
- APIs leves em Flask para focar na comunicação e no gateway.

---
