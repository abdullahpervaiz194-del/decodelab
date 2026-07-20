import random
import string 
length=int(input("Enter the length of the password "))
password=''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Generated password: ",password)
