FROM cibuilds/hugo as builder

RUN mkdir -p /var/www/blog

COPY . /var/www/blog

WORKDIR /var/www/blog

RUN hugo

FROM nginx:1.15-alpine

COPY ./site.conf ./etc/nginx/conf.d/site.conf
COPY ./certbot/conf/live/northerncoding.com/* ./etc/letsencrypt/live/northerncoding.com/
COPY ./certbot/conf/ssl-dhparams.pem /etc/letsencrypt/ssl-dhparams.pem

COPY --from=builder /var/www/blog/public/ /usr/share/nginx/html/blog/