"""Vigenere cipher."""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = []
    for letter in keyword:
        if letter.isupper():
            key.append((ord(letter) - ord("A")) % 26 + ord("A"))
        elif letter.islower():
            key.append((ord(letter) - ord("a")) % 26 + ord("a"))
    key_index = 0
    for letter_index in range(len(plaintext)):
        if key[key_index] == ord("A") or key[key_index] == ord("a"):
            ciphertext += plaintext[letter_index]
        elif plaintext[letter_index].isupper():
            ciphertext += chr(
                (ord(plaintext[letter_index]) + key[key_index]) % 26 + ord("A")
            )
        elif plaintext[letter_index].islower():
            ciphertext += chr(
                (ord(plaintext[letter_index]) + key[key_index]) % 26 + ord("a")
            )
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = []
    for letter in keyword:
        if letter.isupper():
            key.append((ord(letter) - ord("A")) % 26 + ord("A"))
        elif letter.islower():
            key.append((ord(letter) - ord("a")) % 26 + ord("a"))
    key_index = 0
    for letter_index in range(len(ciphertext)):
        if key[key_index] == ord("A") or key[key_index] == ord("a"):
            plaintext += ciphertext[letter_index]
        elif ciphertext[letter_index].isupper():
            plaintext += chr(
                (ord(ciphertext[letter_index]) - key[key_index]) % 26 + ord("A")
            )
        elif ciphertext[letter_index].islower():
            plaintext += chr(
                (ord(ciphertext[letter_index]) - key[key_index]) % 26 + ord("a")
            )
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return plaintext
