def encrypt_vigenere(plaintext: str, key: str) -> str:
    if not key or not key.isalpha():
        raise ValueError("Key phải là chuỗi chữ cái không rỗng")
    
    key = key.upper()
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()
            
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char_upper) - ord('A') + shift) % 26 + ord('A'))
            
            if is_upper:
                ciphertext += encrypted_char
            else:
                ciphertext += encrypted_char.lower()
            
            key_index += 1
        else:
            ciphertext += char
    
    return ciphertext


def decrypt_vigenere(ciphertext: str, key: str) -> str:

    if not key or not key.isalpha():
        raise ValueError("Key phải là chuỗi chữ cái không rỗng")
    
    key = key.upper()
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()
            
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char_upper) - ord('A') - shift) % 26 + ord('A'))
            
            if is_upper:
                plaintext += decrypted_char
            else:
                plaintext += decrypted_char.lower()
            
            key_index += 1
        else:
            plaintext += char
    
    return plaintext