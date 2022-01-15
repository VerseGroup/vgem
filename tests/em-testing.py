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

message = "A very secret message"
print(message)
print()


message = handler.encrypt_rsa(message, True)
print(message)
print()

message = handler.decrypt_rsa(message, True)
print(message)
print()
