import os
import requests
import SSLKeyGenerator


def CreateDefaultCertificates(domain, \
        docker_compose_certbot = 'docker-compose.certbot.yml',
        data_path = './certbot/conf'):

    print("### Preparing directories in {0} ...".format(data_path))
    if not(os.path.isdir(os.path.join(data_path, 'live', domain))):
        os.makedirs(os.path.join(data_path, 'live', domain))

    print("### Creating dummy certificate ...")
    path = os.path.join(data_path, 'live', domain)
    SSLKeyGenerator.create_self_signed_cert(path, 'fullchain.pem', 'privkey.pem')

    print("### Downloading recommended HTTPS parameters ...")
    response = requests.get("https://raw.githubusercontent.com/certbot/certbot/master/certbot/ssl-dhparams.pem")
    SaveToFile(os.path.join(data_path, "ssl-dhparams.pem"), response.text)


def SaveToFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


if __name__ == "__main__":
    rootDomain = 'northerncoding.com'
    docker_compose_certbot = 'docker-compose.certbot.yml'
    CreateDefaultCertificates(rootDomain, docker_compose_certbot)