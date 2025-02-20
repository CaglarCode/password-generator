import secrets
import string

def generate_secure_key(length=43):
    characters = string.ascii_letters + string.digits + "+/="
    return ''.join(secrets.choice(characters) for _ in range(length))

print("Generated Key:", generate_secure_key())
