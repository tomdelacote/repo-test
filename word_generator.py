import string
import random

print("Word Generator")

alphabet = string.ascii_lowercase

word = "bruh"

for i in range(random.randint(3, 8)):
    word += random.choice(alphabet)
    
print(word)

