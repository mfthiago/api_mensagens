#!/bin/bash

echo "🔧 Iniciando build dos containers..."
docker-compose up --build -d

echo "⏳ Aguardando inicialização dos serviços..."
sleep 10

echo "🧪 Testando API Record-API..."

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5001/messages)

if [ "$STATUS" -eq 200 ]; then
    echo "✅ Record-API está respondendo corretamente (Status $STATUS)"
else
    echo "❌ Erro ao testar a Record-API (Status $STATUS)"
    exit 1
fi

echo "🚀 Serviços iniciados com sucesso!"
