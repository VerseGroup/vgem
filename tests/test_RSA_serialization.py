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
handler = EM()

def test_serialization():
    message = "SECRET MESSAGE"
    emessage = handler.encrypt_rsa(message, True)
    private_key = handler.serialize_private_key()

    handler2 = EM(serialized_private_key=private_key)
    dmessage = handler2.decrypt_rsa(emessage, True)

    assert message == dmessage
  
