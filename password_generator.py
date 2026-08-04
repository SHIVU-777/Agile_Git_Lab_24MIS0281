import random
chars = "abcdefghijklmnopqrstuvwxyz123456789"
password = "".join(random.choice(chars) for i in range(8))
print(password)