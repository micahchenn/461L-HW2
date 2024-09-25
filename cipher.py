# cipher.py
# Homework 2
# Micah Chen (mc75458)

'''
TASK 1
'''
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

'''
TASK 2
'''
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




















''' ----------------
TASK 3 functions
----------------'''

# Function to read the database from the file
def read_database(filename):
    database = {}
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()
            if ' ' in line:
                try:
                    userid, password = line.split(' ', 1)  # Split by space instead of comma
                    database[userid] = password
                except ValueError:
                    print(f"Skipping invalid line: {line}")
            else:
                print(f"Skipping invalid line: {line}")
    return database



# Function to check credentials against the table data
def check_credentials(database, table_data, N, D):
    matched_combinations = []
    mismatched_passwords = []
    invalid_userids = []

    for encrypted_userid, encrypted_password in database.items():
        # Decrypt the userid and password from the database
        decrypted_userid = decrypt(encrypted_userid, N, D)
        decrypted_password = decrypt(encrypted_password, N, D)

        print(f"Decrypted userid: {decrypted_userid}, Decrypted password: {decrypted_password}")

        # Check if the decrypted userid matches the one in the table_data
        if decrypted_userid in table_data:
            if table_data[decrypted_userid] == decrypted_password:
                matched_combinations.append((decrypted_userid, decrypted_password))
            else:
                mismatched_passwords.append(decrypted_userid)
        else:
            invalid_userids.append(decrypted_userid)
    
    return matched_combinations, mismatched_passwords, invalid_userids


# Main test code
if __name__ == "__main__":
    # Load the database
    database = read_database('database.txt')

    # Decryption parameters (from task description)
    N = 3  # Number of shifts
    D = 1  # Shift direction (1 = right, -1 = left)

    # The table data with userids and passwords
    table_data = {
        'asamant': 'Temp123',
        'aissa': 'TheKing%^&',
        'bjha': '$72messenger',
        'skharel': 'Life15$',
        'Ally!': 'God$12'
    }

    # Check credentials and print results
    matches, mismatches, invalids = check_credentials(database, table_data, N, D)

    print(f"Matching userids and passwords: {matches}")
    print(f"Userids with mismatched passwords: {mismatches}")
    print(f"Invalid userids: {invalids}")



'''
TASK 3: 
1. Which of the userid and password combination(s) in the table above are present in the d
atabase?
2. Which userid(s) is/are present in the database, but the password does not match the pa
ssword(s) in the table above?
3. Which userid(s) do/does not meet the requirements of a userid?

Decrypted userid: asamant, Decrypted password: Temp123
Decrypted userid: aissa, Decrypted password: Light%^&
Decrypted userid: bjha, Decrypted password: $72Hello
Decrypted userid: skharel, Decrypted password: Life15$
Decrypted userid: Ally, Decrypted password: God$12
1. Matching userids and passwords: [('asamant', 'Temp123'), ('skharel', 'Life15$')]
2. Userids with mismatched passwords: ['aissa', 'bjha']
3. Invalid userids: ['Ally']

'''

