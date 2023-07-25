import random
import string 
def code_generator(length):
    code=""
    characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz1234567890@#$%^&*"
    for _ in range(length):
        code+=random.choice(characters)
    return code
code_length=int(input("enter the pasword length: "))
generated_code=code_generator(code_length)
print("generated code :",generated_code)



