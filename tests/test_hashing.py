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
    hash = handler.hash(message, True)
    assert handler.check_hash(message, hash, True)