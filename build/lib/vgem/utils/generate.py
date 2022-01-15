# crypto imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# generates a new connected private and public key (as objects)
def generate_private():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def generate_public(private_key):
    return private_key.public_key()