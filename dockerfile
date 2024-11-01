# Usa la imagen oficial de Nginx
FROM nginx:alpine

# Copia el archivo HTML al directorio de Nginx
COPY index.html /usr/share/nginx/html/index.html

# Exponer el puerto 80
EXPOSE 80

# Inicia nginx
CMD ["nginx", "-g", "daemon off;"]
