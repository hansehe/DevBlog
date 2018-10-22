from OpenSSL import crypto, SSL
from socket import gethostname
from pprint import pprint
from time import gmtime, mktime
import os

# Ref: https://skippylovesmalorie.wordpress.com/2010/02/12/how-to-generate-a-self-signed-certificate-using-pyopenssl/
def CreateSelfSignedCert(cert_dir = "SSLKeys", cert_file = "fullchain.pem", key_file = "privkey.pem"):
    """
    If datacard.crt and datacard.key don't exist in cert_dir, create a new
    self-signed cert and keypair and write them into that directory.
    """

    if not os.path.exists(cert_dir):
        os.makedirs(cert_dir)

    if not os.path.exists(os.path.join(cert_dir, cert_file)) \
            or not os.path.exists(os.path.join(cert_dir, key_file)):
            
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "US"
        cert.get_subject().ST = "Minnesota"
        cert.get_subject().L = "Minnetonka"
        cert.get_subject().O = "my company"
        cert.get_subject().OU = "my organization"
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')

        open(os.path.join(cert_dir, cert_file), "wb").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(os.path.join(cert_dir, key_file), "wb").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

if __name__ == "__main__":
    CreateSelfSignedCert()
    
