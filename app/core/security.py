from cryptography.fernet import Fernet
import base64

# Generate a key for encryption and decryption
KEY = Fernet.generate_key()

# Instance the Fernet class with the key
FERNET = Fernet(KEY)

def hash_password(password: str) -> str:
    # Encrypt the password and encode the result in base64
    encrypted_password = FERNET.encrypt(password.encode())
    return base64.b64encode(encrypted_password).decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Decode the base64 and then decrypt the password
    decoded_hash = base64.b64decode(hashed_password.encode())
    decrypted_password = FERNET.decrypt(decoded_hash).decode()
    return plain_password == decrypted_password
