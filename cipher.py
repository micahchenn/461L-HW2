# cipher.py

# Encrypt function
def encrypt(inputText: str, N: int, D: int) -> str:
    if D not in [-1, 1]:
        raise ValueError("Invalid direction, must be -1 or 1")
    
    # Step 1: Reverse the input text
    reversed_text = inputText[::-1]
    encrypted_text = ""
    
    for char in reversed_text:
        ascii_value = ord(char)
        
        # Skip space and !
        if ascii_value in (32, 33):
            encrypted_text += char
        else:
            # Apply shift with wrap-around, skipping space and !
            shifted_value = ascii_value + (N * D)
            if shifted_value < 34:
                shifted_value = 126 - (33 - shifted_value)
            elif shifted_value > 126:
                shifted_value = 34 + (shifted_value - 127)
            
            encrypted_text += chr(shifted_value)
    
    return encrypted_text


# Decrypt function
def decrypt(encryptedText: str, N: int, D: int) -> str:
    if D not in [-1, 1]:
        raise ValueError("Invalid direction, must be -1 or 1")
    
    decrypted_text = ""
    
    for char in encryptedText:
        ascii_value = ord(char)
        
        # Skip space and !
        if ascii_value in (32, 33):
            decrypted_text += char
        else:
            # Reverse shift with wrap-around
            shifted_value = ascii_value - (N * D)
            if shifted_value < 34:
                shifted_value = 126 - (33 - shifted_value)
            elif shifted_value > 126:
                shifted_value = 34 + (shifted_value - 127)
            
            decrypted_text += chr(shifted_value)
    
    # Reverse the text back to original
    return decrypted_text[::-1]
