def encrypt(text: str, method: str = "Caesar") -> str:
    # TODO: партнер реалізує кожен алгоритм
    if method == "Caesar":
        return text[::-1]  # заглушка
    elif method == "AES-256":
        return text[::-1]  # заглушка
    elif method == "RSA":
        return text[::-1]  # заглушка
    return text


def decrypt(text: str, method: str = "Caesar") -> str:
    # TODO: партнер реалізує кожен алгоритм
    if method == "Caesar":
        return text[::-1]  # заглушка
    elif method == "AES-256":
        return text[::-1]  # заглушка
    elif method == "RSA":
        return text[::-1]  # заглушка
    return text