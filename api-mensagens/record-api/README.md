# Record-API

API responsável pelo armazenamento e consulta de mensagens no sistema de chat distribuído.

---

## 🐳 Como rodar?

Clone ou baixe o projeto. Depois, abra a pasta `record-api` no terminal e execute:

```bash
docker-compose up --build
```

Esse comando irá subir a API Python (Flask) com todas as dependências já instaladas, juntamente com os serviços de banco de dados MySQL e cache Redis.  

> ⚠️ Verifique se as portas `5001`, `3306` (MySQL) ou `6379` (Redis) estão livres. Caso contrário, encerre os processos que estão usando essas portas ou edite o arquivo `docker-compose.yml`.

---

## 📦 Endpoints

### [GET] `/messages`

Retorna todas as mensagens armazenadas no sistema.

**URL:**
```
http://localhost:5001/messages
```

**Exemplo de resposta:**
```json
[
  {
    "id": 1,
    "content": "Mensagem teste do Ibrahim"
  }
]
```

> 🔄 **Usa cache Redis**: ao consultar pela primeira vez, os dados são buscados do banco e armazenados no Redis. Nas próximas requisições, a resposta vem diretamente do cache.

---

### [POST] `/messages`

Registra uma nova mensagem no banco de dados.

**URL:**
```
http://localhost:5001/messages
```

**Body esperado:**
```json
{
  "content": "Mensagem teste do Ibrahim"
}
```

**Resposta esperada:**
```json
{
  "content": "Mensagem teste do Ibrahim"
}
```

> ⚠️ Ao criar uma nova mensagem, o cache Redis é automaticamente limpo para garantir que a próxima consulta retorne os dados atualizados.

---

## 🚀 Tecnologias utilizadas

- Python 3.10
- Flask
- MySQL 8.0
- Redis
- Docker
- Docker Compose

---

## 📂 Estrutura de diretórios

```bash
record-api/
├── config/
│   ├── cache.py
│   └── database.py
├── src/
│   ├── controllers/
│   ├── exceptions/
│   ├── models/
│   ├── repositories/
│   └── services/
├── deploy.sh
├── docker-compose.yml
├── Dockerfile
├── index.py
├── README.md
└── router.py
```

---

## 🛠️ Observações finais

- A tabela `messages` é esperada no banco `chat`. Caso não exista, crie com:

```sql
CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT NOT NULL
);
```

- Redis é usado como camada de cache inteligente para reduzir as consultas no banco.

---