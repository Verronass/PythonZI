import os

ENCRYPTED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "first.txt")

def decrypt(key: str = "") -> str:
    if not os.path.exists(ENCRYPTED_FILE):
        return "Файл first.txt не знайдено"
    if not key:
        return "Введіть ключ"
    with open(ENCRYPTED_FILE, "rb") as f:
        encrypted_data = f.read()
    key_bytes = key.encode("utf-8")
    decrypted = bytearray()
    for i in range(len(encrypted_data)):
        decrypted.append(encrypted_data[i] ^ key_bytes[i % len(key_bytes)])
    try:
        return decrypted.decode("utf-8")
    except Exception:
        return "Невірний ключ"