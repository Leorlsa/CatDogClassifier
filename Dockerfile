# Use uma imagem base oficial do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o contêiner
COPY . .

# Exponha a porta que a aplicação vai usar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
