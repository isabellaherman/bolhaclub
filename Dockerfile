# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copie todos os arquivos do seu host para o diretório atual no container 
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que sua aplicação usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python3", "server/app.py"]