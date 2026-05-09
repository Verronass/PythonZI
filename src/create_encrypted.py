import os

# Оригінальний текст
original_text = "Ми будемо дуже раді, якщо ти вступиш до нас"
key = "OpenDayZi"

# Шифруємо
key_bytes = key.encode('utf-8')
original_bytes = original_text.encode('utf-8')
encrypted_result = bytearray()

for i in range(len(original_bytes)):
    encrypted_result.append(original_bytes[i] ^ key_bytes[i % len(key_bytes)])

# Зберігаємо зашифрований файл
with open("first.txt", "wb") as f:
    f.write(encrypted_result)

print(f"Зашифрований файл створено: {encrypted_result.hex()}")
