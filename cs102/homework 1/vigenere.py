def encrypt_vigenere(plaintext, keyword) -> str:
    """
       >>> encrypt_vigenere("PYTHON", "A")
       'PYTHON'
       >>> encrypt_vigenere("python", "a")
       'python'
       >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
       'LXFOPVEFRNHR'
       """
    ciphertext = ''
    i = 0
    for ch in plaintext:

        if ch.isalpha():
            shift = ord(keyword[i % len(keyword)])
            if 'a' <= chr(shift) <= 'z':
                shift -= ord('a')
            else:
                shift -= ord('A')
            code = ord(ch) + shift
            if 'a' < ch < 'z' and code > ord('z'):
                code -= 26
            elif 'A' < ch < 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += ch
        i = 1 + i
    return ciphertext


def decrypt_vigenere(ciphertext, keyword) -> str:
    """
        >>> decrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> decrypt_vigenere("python", "a")
        'python'
        >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
        'ATTACKATDAWN'
        """
    plaintext = ''
    i = 0;
    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[i % len(keyword)])
            if 'a' <= chr(shift) <= 'z':
                shift -= ord('a')
            else:
                shift -= ord('A')
            code = ord(ch) - shift
            if 'a' < ch < 'z' and code < ord('a'):
                code += 26
            elif 'A' < ch < 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ch
        i = 1 + i
    return plaintext


plaintext = str(input('Your message: '))
keyword = str(input('Keywordd: '))

ciphertext = encrypt_vigenere(plaintext, keyword)
print("Cod: " + ciphertext)
print("Not Cod: " + decrypt_vigenere(ciphertext, keyword))
