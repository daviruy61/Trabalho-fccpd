# Imagem base leve para rodar aplicação Python
FROM python:3.11-slim

# Diretório base do código dentro do container
WORKDIR /app

# Instala as bibliotecas necessárias para o microsserviço
RUN pip install --no-cache-dir Flask requests

# Copia o arquivo principal da API
COPY app.py .

# Porta exposta para acesso ao Serviço B
EXPOSE 5001

# Comando padrão para iniciar a aplicação Flask
CMD ["python", "app.py"]
