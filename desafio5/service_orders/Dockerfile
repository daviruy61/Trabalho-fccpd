# Imagem base leve para executar aplicações Python
FROM python:3.11-slim

# Define o diretório principal no container
WORKDIR /app

# Instala o Flask para exposição da API HTTP
RUN pip install --no-cache-dir Flask

# Copia o arquivo da aplicação para o container
COPY app.py .

# Porta em que o serviço de pedidos escuta
EXPOSE 5001

# Comando de inicialização da aplicação Flask
CMD ["python", "app.py"]
