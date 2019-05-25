import os
import requests
import subprocess
import shutil
import time


def InitLetsencrypt(domain, \
        staging = True, \
        email = '', \
        data_path = './certbot',
        docker_compose_nginx = 'docker-compose.nginx.yml', \
        docker_compose_certbot = 'docker-compose.certbot.yml',
        rsa_key_size = 4096):

    print("### Preparing directories in {0} ...".format(data_path))
    shutil.rmtree(data_path, True)
    os.makedirs(os.path.join(data_path, 'www'))
    os.makedirs(os.path.join(data_path, 'conf', 'live', domain))

    print("### Creating dummy certificate ...")
    path = '/etc/letsencrypt/live/{0}'.format(domain)
    command = "docker-compose -f {0} run --rm --entrypoint \
    \"openssl req -x509 -nodes -newkey rsa:1024 -days 1\
      -keyout '{1}/privkey.pem' \
      -out '{1}/fullchain.pem' \
      -subj '/CN=localhost'\" certbot".format(docker_compose_certbot, path)
    ExecuteTerminalCommand(command)

    print("### Downloading recommended HTTPS parameters ...")
    response = requests.get("https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf")
    SaveToFile(os.path.join(data_path, "conf/options-ssl-nginx.conf"), response.text)
    response = requests.get("https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem")
    SaveToFile(os.path.join(data_path, "conf/ssl-dhparams.pem"), response.text)

    print("### Starting nginx ...")
    command = "docker-compose -f {0} pull".format(docker_compose_nginx)
    ExecuteTerminalCommand(command)
    command = "docker-compose -f {0} up -d nginx".format(docker_compose_nginx)
    ExecuteTerminalCommand(command)
    time.sleep(2)

    print("### Deleting dummy certificate ...")
    shutil.rmtree(os.path.join(data_path, 'conf/live'), True)

    print("### Requesting initial certificate ...")

    staging_arg = ''
    if staging:
        staging_arg = '--staging'

    email_arg = '--register-unsafely-without-email'
    if len(email) > 0:
        email_arg = '--email {0}'.format(email)

    domain_arg = '-d {0}'.format(domain)

    command = "docker-compose -f {0} run --rm --entrypoint \"\
            certbot certonly --webroot -w /var/www/certbot \
            {1} \
            {2} \
            {3} \
            --rsa-key-size {4} \
            --agree-tos \
            --force-renewal\" certbot".format(docker_compose_certbot, \
                staging_arg, \
                email_arg, \
                domain_arg, \
                rsa_key_size)
    ExecuteTerminalCommand(command)
    time.sleep(2)

    command = "docker-compose -f {0} stop nginx".format(docker_compose_nginx)
    ExecuteTerminalCommand(command)


def ExecuteTerminalCommand(terminalCommand):
    print("Executing: " + terminalCommand)
    subprocess.Popen(terminalCommand, shell=True).wait()


def SaveToFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    domain = 'northerncoding.com'
    email = 'hans.erik.heggem@gmail.com'
    staging = True
    InitLetsencrypt(domain, staging, email)