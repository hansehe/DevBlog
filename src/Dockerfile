FROM cibuilds/hugo as builder

RUN mkdir -p /var/www/blog

COPY . /var/www/blog

WORKDIR /var/www/blog

RUN hugo

FROM nginx

COPY ./nginx.ssl.conf ./etc/nginx/conf.d/site.conf

COPY --from=builder /var/www/blog/public/ /usr/share/nginx/html/