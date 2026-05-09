import os

ENCRYPTED_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "first.txt")

def get_encrypted_content() -> str:
    """Повертає зашифрований вміст у шістнадцятковому форматі"""
    if not os.path.exists(ENCRYPTED_FILE):
        return "Файл first.txt не знайдено"
    with open(ENCRYPTED_FILE, "rb") as f:
        encrypted_data = f.read()
    return encrypted_data.hex()

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
        # Якщо не вдалося розшифрувати, шифруємо оригінальний текст новим ключем
        return encrypt_with_key(key)

def encrypt_with_key(key: str) -> str:
    """Шифрує оригінальний текст з новим ключем"""
    original_text = "Ми будемо дуже раді, якщо ти вступиш до нас"
    key_bytes = key.encode("utf-8")
    original_bytes = original_text.encode("utf-8")
    encrypted_result = bytearray()
    
    for i in range(len(original_bytes)):
        encrypted_result.append(original_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    # Повертаємо зашифрований текст у шістнадцятковому форматі
    return encrypted_result.hex()