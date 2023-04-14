import hashlib

from env import CRYPTO_SALT


async def encrypt_data(data: str):
    return hashlib.sha256((data + CRYPTO_SALT).encode()).hexdigest()
