from pwdlib import PasswordHash
from pwdlib import PasswordHash


def hash_password(password: str) -> str:

    password_hash = PasswordHash.recommended()
    return password_hash.hash(password)
def verify_password(plain_password, hashed_password):
    password_hash = PasswordHash.recommended()
    return password_hash.verify(plain_password, hashed_password)