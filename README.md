# vgem (python edition)
A wrapper for python's cryptography package using OOP principals. 

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

### New
- hashing and salting!





