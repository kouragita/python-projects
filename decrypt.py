import requests
from cryptography.fernet import Fernet

# Load decryption key
decryption_key = 'b_VBjrWt90'

# Retrieve encrypted data from HTTPS link
url = 'https://ehi.link/b_VBjrWt90'
response = requests.get(url)
encrypted_data = response.content

# Create Fernet object
cipher_suite = Fernet(decryption_key)

# Decrypt and decode data
decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')

# Use the decrypted data as needed
print(decrypted_data)
