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

def test_fernet_serialization():

    message = "A very secret message"

    emessage = handler.encrypt_fernet(message, True)

    key = handler.serialize_fernet(True, True)

    private_key = handler.serialize_private_key()

    handler2 = EM(serialized_private_key=private_key, encrypted_fernet_key=key)

    dmessage = handler2.decrypt_fernet(emessage, True)

    assert message == dmessage
