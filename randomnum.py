import random

def generate_phone_number():
    phone_number = ''.join(random.choice('0123456789') for _ in range(10))
    return phone_number

# Call the function to generate and print a phone number
phone_number = generate_phone_number()
print(phone_number)
