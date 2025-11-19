# Usa uma imagem base Nginx muito leve
FROM nginx:alpine

# Copia o seu index.html (e quaisquer outros assets se houverem) para o local de servir do Nginx
COPY index.html /usr/share/nginx/html/index.html

# Nginx escuta a porta 80 por padrão. O Cloud Run precisa da porta 8080.
# Vamos usar o NGINX_PORT como variável de ambiente para ser flexível.
ENV NGINX_PORT 8080
EXPOSE 8080

# Comando para rodar o Nginx, escutando a porta 8080 (a porta $PORT no Cloud Run)
CMD ["nginx", "-g", "daemon off;"]