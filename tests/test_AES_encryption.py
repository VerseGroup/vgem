# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# local imports
from vgem import EM
handler = EM()

def test_AES_encryption():
    message = "A very secret message"

    emessage = handler.encrypt_aes(message, True)

    dmessage = handler.decrypt_aes(emessage, True)

    assert dmessage == message

