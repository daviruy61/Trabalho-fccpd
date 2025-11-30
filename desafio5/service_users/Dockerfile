# Imagem base enxuta com suporte a Python 3.11
FROM python:3.11-slim

# Diretório de trabalho da aplicação
WORKDIR /app

# Instalação do microframework web utilizado
RUN pip install --no-cache-dir Flask

# Copia o código-fonte para dentro do container
COPY app.py .

# Porta exposta pelo serviço de usuários
EXPOSE 5000

# Comando padrão para iniciar a API Flask
CMD ["python", "app.py"]
