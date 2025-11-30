# Imagem base enxuta com Python 3.11
FROM python:3.11-slim

# Diretório interno da aplicação
WORKDIR /app

# Instalação da dependência necessária para a API
RUN pip install --no-cache-dir Flask

# Copia o código-fonte para dentro da imagem
COPY app.py .

# Porta utilizada pelo serviço Flask
EXPOSE 5000

# Processo principal do container
CMD ["python", "app.py"]
