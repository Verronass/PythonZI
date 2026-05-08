def encrypt(text: str, method: str = "Caesar", key: str = "") -> str:
    # TODO: партнер реалізує логіку
    if method == "Caesar":
        return text[::-1]
    elif method == "AES-256":
        return text[::-1]
    elif method == "RSA":
        return text[::-1]
    return text


def decrypt(text: str, method: str = "Caesar", key: str = "") -> str:
    # TODO: партнер реалізує логіку
    if method == "Caesar":
        return text[::-1]
    elif method == "AES-256":
        return text[::-1]
    elif method == "RSA":
        return text[::-1]
    return text