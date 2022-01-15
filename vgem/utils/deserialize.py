# crypto imports
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def deserialize_private_key(serialized_private_key):
    private_key = serialization.load_pem_private_key(
        serialized_private_key,
        password=None,
        backend=default_backend()
    )
    return private_key

def deserialize_public_key(serialized_public_key):
    public_key = serialization.load_pem_public_key(
        serialized_public_key,
        backend=default_backend()
    )
    return public_key
