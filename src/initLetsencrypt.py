import os
import subprocess
import shutil
import time
import argparse


def InitLetsencrypt(domains, \
        staging = True, \
        email = '', \
        docker_compose_certbot = 'docker-compose.certbot.yml',
        data_path = './certbot',
        rsa_key_size = 4096):

    print("### Requesting initial certificate ...")

    staging_arg = ''
    if staging:
        staging_arg = '--staging'

    email_arg = '--register-unsafely-without-email'
    if len(email) > 0:
        email_arg = '--email {0}'.format(email)

    domain_arg = ''
    for domain in domains:
        domain_arg += '-d {0} '.format(domain)

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


def ExecuteTerminalCommand(terminalCommand):
    print("Executing: " + terminalCommand)
    subprocess.Popen(terminalCommand, shell=True).wait()


def GenerateDomains(rootDomain, subdomains):
    domains = []
    domains.append(rootDomain)
    for subdomain in subdomains:
        domains.append(subdomain + '.' + rootDomain)
    return domains


if __name__ == "__main__":
    rootDomain = 'northerncoding.com'
    subdomains = ['demo', 'portainer']
    email = ''
    docker_compose_certbot = 'docker-compose.certbot.yml'

    parser = argparse.ArgumentParser()
    parser.add_argument("--no-staging",
                        help="Add --no-staging to fetch real certificates.",
                        action='store_true')
    arguments = parser.parse_args()
    staging = not(arguments.no_staging)

    domains = GenerateDomains(rootDomain, subdomains)
    InitLetsencrypt(domains, staging, email, docker_compose_certbot)