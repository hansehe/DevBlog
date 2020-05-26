FROM cibuilds/hugo:0.71.1 as builder

USER root

COPY . /var/www/blog

WORKDIR /var/www/blog

RUN hugo

FROM nginx:1.15-alpine

COPY ./app.conf ./etc/nginx/conf.d/site.conf
# COPY ./app_ssl.conf ./etc/nginx/conf.d/site.conf

COPY --from=builder /var/www/blog/public/ /usr/share/nginx/html/blog/