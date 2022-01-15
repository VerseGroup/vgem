# python imports
import base64

# base64 converts binary (encrypted messages are typically binary) to reasonably strings 
# to ensure it doesn't get altered when networking, and is not a form of encryption

def encode(message):
    coded_message = base64.b64encode(message)
    coded_message = coded_message.decode('utf-8')
    return coded_message

def decode(coded_message):
    coded_message = coded_message.encode('utf-8')
    message = base64.b64decode(coded_message)
    return message
