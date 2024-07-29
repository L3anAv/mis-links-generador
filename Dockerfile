# Utiliza una imagen base de Node.js
FROM node:16-alpine

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de tu proyecto
COPY package*.json ./
RUN npm install
COPY . .

# Exponer el puerto 5000 y mapearlo al puerto 3000
EXPOSE 5000:3000

# Comando para iniciar tu aplicación
CMD ["node", "index.js"]