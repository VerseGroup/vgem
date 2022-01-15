# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# local imports
from vg_em import EM
handler = EM()

def encrypt(message):
    emessage = handler.encrypt_rsa(message, True)
    return emessage

def decrypt(emessage):
    dmessage = handler.decrypt_rsa(emessage, True)
    return dmessage


def test_encryption():
    message = "A very secret message"
    
    emessage = encrypt(message)
    dmessage = decrypt(emessage)

    assert message == dmessage

