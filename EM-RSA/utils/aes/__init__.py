# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)

# local imports for shorter routes
from generate import generate_cipher
from encrypt import encrypt_aes
from decrypt import decrypt_aes