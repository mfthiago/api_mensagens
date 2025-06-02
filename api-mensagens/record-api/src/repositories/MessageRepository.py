from config.database import get_db
from config.cache import get_cache
import json

class MessageRepository:
    def __init__(self):
        self.cache = get_cache()

    def get_all(self):
        cache_key = "messages:all"

        # Tenta pegar do cache Redis
        cached = self.cache.get(cache_key)
        if cached:
            print("🧠 Dados vindos do Redis!")
            return json.loads(cached)

        # Se não encontrar, busca no banco de dados
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM messages")
        rows = cursor.fetchall()
        result = [dict(id=row[0], content=row[1]) for row in rows]

        # Armazena no cache por 60 segundos
        self.cache.setex(cache_key, 60, json.dumps(result))
        print("💾 Dados salvos no Redis!")
        return result

    def create(self, data):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO messages (content) VALUES (%s)", (data['content'],))
        db.commit()

        # Invalida o cache após inserir nova mensagem
        self.cache.delete("messages:all")
        return {'content': data['content']}
