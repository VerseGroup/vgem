# Encryption Manager (python edition)
VerseGroup's native encryption manager adapted for python applications.

## Function
EM is an efficient manager to allow for easy encryption/decryption/secure session management, without having to code for specific algorithims, as
long as the client/reciever uses this same package (or alternative language equivalent)

EM prefers the OOP approach, in order to reduce the amount of key passing and similar tedious tasks

## RSA and AES explained

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
- Base64 encoding prefered as cipher is typically binary





