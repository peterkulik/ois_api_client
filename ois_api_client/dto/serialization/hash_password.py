from hashlib import sha512


def hash_password(password: str) -> str:
    ut8_encoded = password.encode('UTF-8', 'strict')
    result = sha512(ut8_encoded).hexdigest().upper()
    return result
