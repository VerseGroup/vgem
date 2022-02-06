# python imports
import os
import sys
from tabnanny import check

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# local imports
from vgem import EM
handler = EM()

def test_hashing():
    hash = handler.hash("A very secret message", True)
    assert True

def test_hash_check():
    message = "A very secret message"
    dict = handler.hash(message, True)
    hash = dict['hash']
    salt = dict['salt']
    try: 
        result = handler.check_hash(message=message, hash=hash, salt=salt, base64=True)
        assert True
    except:
        assert False