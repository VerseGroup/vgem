# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# local imports
from src import EM
from t_RSA_encryption import test_encryption

handler = EM()

private_key = handler.serialize_private_key()
print(f"PRIVATEKEY: {private_key}")
print()

public_key = handler.serialize_public_key()
print(f"PUBLICKEY: {public_key}")
print()

handler2 = EM(serialized_private_key=private_key)
test_encryption(handler2)
