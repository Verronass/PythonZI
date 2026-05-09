import base64
import os
import tkinter as tk

# Оригінальний текст
original_text = "Ми будемо дуже раді, якщо ти вступиш до нас"

key = input("Введи ключ: ")
key_bytes = key.encode('utf-8')
expected_key = "OpenDayZi"

# Шифруємо оригінальний текст
original_bytes = original_text.encode('utf-8')
encrypted_result = bytearray()
for i in range(len(original_bytes)):
    encrypted_result.append(original_bytes[i] ^ key_bytes[i % len(key_bytes)])

# Зберігаємо зашифрований текст у first.txt
with open("first.txt", "wb") as f:
    f.write(encrypted_result)

# Виводимо зашифрований вміст
print(f"Зашифрований вміст файлу: {encrypted_result.hex()}")

# Читаємо зашифрований файл
with open("first.txt", "rb") as f:
    encrypted_data = f.read()

# Перевіряємо ключ і розшифровуємо
if key == expected_key:
    # Розшифровуємо з правильним ключем
    decrypted_result = bytearray()
    for i in range(len(encrypted_data)):
        decrypted_result.append(encrypted_data[i] ^ key_bytes[i % len(key_bytes)])
    
    decrypted_text = decrypted_result.decode('utf-8')
    print(f"\nРозшифрований текст: {decrypted_text}")
    print("Ключ правильний! Файл успішно розшифровано.")
else:
    # Неправильний ключ - шифруємо ще раз з новим ключем
    print(f"Ключ неправильний. Повторно шифруємо з ключем: {key}")
    
    new_encrypted = bytearray()
    for i in range(len(original_bytes)):
        new_encrypted.append(original_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    with open("result.txt", "wb") as f:
        f.write(new_encrypted)
    
    print(f"Файл зашифровано в result.txt ключем: {key}")
    print(f"Новий зашифрований вміст: {new_encrypted.hex()}")
