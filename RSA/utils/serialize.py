# crypto imports
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# serialization is converting the local objects into strings or 
# JSON to be shipped over a network

# this package uses base64 encoded PEM to ship

def serialize_private_key(private_key):
    serialized_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
        ) 
    return serialized_private_key

def serialize_public_key(public_key):
    serialized_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    return serialized_public_key