# vgem (python edition)
VerseGroup's native encryption manager adapted for python applications.

## Function
EM is an efficient manager to allow for easy encryption/decryption/secure session management, without having to code for specific algorithims, as
long as the client/reciever uses this same package (or alternative language equivalent). 

EM prefers the OOP approach, in order to reduce the amount of key passing and similar tedious tasks. Simply initiate an EM instance empty to generate a new set of keys, or pass in existing keys (serialized or object formatted) to use. Supports mainly RSA assymetric encryption, but also hybrid encryption with RSA generated AES sessions. 

## RSA and AES explained

## How to Use

Through terminal with an activated virtualenv:
~~~
pip install vgem
~~~

In python:
~~~
from vgem.em import EM
~~~

Then you have access to the EM class. 
Example usage:
~~~
from vgem.em import EM

handler = EM()

essage = "A very secret message"

encrypted_message = handler.encrypt(message)

private_key = handler.serialize_private_key()

handler2 = EM(serialized_private_key = private_key)

decrypted_message = handler2.decrypt(encrypted_message)

assert message == decrypted_message
~~~

## Documentation
class EM
utils (all EM functions, disorganized)

### Attributes
- RSA private key
- RSA public key
- AES cipher object (consists of key and iv)

### Construction
- Optional Paramaters:
    - RSA private key
    - RSA public key
    - Serialized RSA private key
    - Serialized RSA public key
    - AES cipher key
    - AES cipher iv
- EM will construct anything else essential and not passed in

### Methods
- Serialize private/public RSA keys
- Encrypt/Decrypt using RSA keys
- Start AES session
- Encrypt/Decrypt using AES session
- Serialize/Deserialize RSA encrypted AES keys
- Base64 encoding option for all encrypting and serialization





