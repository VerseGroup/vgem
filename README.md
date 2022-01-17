# vgem (python edition)
VerseGroup's native encryption manager adapted for python applications.

## Function
EM is an efficient manager to allow for easy encryption/decryption/secure session management, without having to code for specific algorithims, as long as the client/reciever uses this same package (or alternative language equivalent). 

EM prefers the OOP approach, in order to reduce the amount of key passing and similar tedious tasks. Simply initiate an EM instance empty to generate a new set of keys, or pass in existing keys (serialized or object formatted) to use. Supports mainly RSA assymetric encryption, but also hybrid encryption with RSA generated fernet wrapped AES sessions. 

## RSA and Fernet-AES explained

RSA is assymetric encryption, which uses private and public keys to send encrypted messages. Private keys can decrypt messages and public keys can only encrypt messages. A server wishing to recieve encrypted messages would distribute its public keys freely, and then decrypt incoming messages with its' private key. For two-way encryption, two servers would each send eachother their public keys, and decrypt messages with their private keys. 

Symmetric keys is less secure as it uses one key that can both encrypt and decrypt. RSA is efficient and more secure than fernet, but can sometime be slow and tedious. So, hybrid encryption is an option. Both servers use their RSA keys to send eachother a symmetric key to use (fernet key) and they then communicate with that fernetkey that only they know (this uses RSA to securly send over the symmteric key).

vgem's EM class supports both use cases.

## How to Use

Through terminal with an activated virtualenv:
~~~
pip install vgem
~~~

In python:
~~~
from vgem import EM
~~~

Then you have access to the EM class. 

Example usage of RSA:
~~~
from vgem import EM

handler = EM()

message = "A very secret message"

encrypted_message = handler.encrypt(message)

private_key = handler.serialize_private_key()

handler2 = EM(serialized_private_key = private_key)

decrypted_message = handler2.decrypt(encrypted_message)

assert message == decrypted_message
~~~

## Documentation
class EM

utils subdir for alternative approach (OOP prefered instead though)

### Attributes
- RSA private key
- RSA public key
- Fernet object
- Fernet key

### Construction
- Optional Paramaters:
    - RSA private key
    - RSA public key
    - Serialized RSA private key
    - Serialized RSA public key
    - Fernet key
    - Encrypted fernet key
- EM will construct anything else essential and not passed in

### Methods
- Serialize private/public RSA keys
- Encrypt/Decrypt using RSA keys
- Load new fernet sessions
- Encrypt/Decrypt using fernet session
- Serialize/Deserialize RSA encrypted fernet keys
- Base64 encoding option for all encrypting and serialization





