# Encryption Manager (python edition)
VerseGroup's native encryption manager adapted for python applications.

## Function
- Generate new set of private and public keys
- Encrypt using private and public keys
- Decrypt using private keys
- Encode in base64 for networking with encrypted messages 

## Implementation
- VerseGroup's Encryption Manager uses an object oriented approach, so encryption will take place through methods and attribute within a class

## Documentation
class EncryptionManager

### Attributes
- private key
- public key

### Methods
- serialize and deserialize private and public keys
- encrypt/decrypt using self's keys

### Construction
- Initialize using either preexisting keys in any format or generate a new  set of keys

## To Add
- Modern architecture also uses SHA to sign AES encrypted messages, as RSA has size limitations. Instead RSA is used to send over an AES symmetric key for a singular session, and then further message's are sent with the AES key and signed in SHA by the RSA private key. 
