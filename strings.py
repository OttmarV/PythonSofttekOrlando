print('Hello World')
print("Hello World")
print("Tony's book")
print("Carlos alias el \"Nato\"")
print(r"Tony's book")
print('''
erkjferwf
''')

spam = "    hola mundo    "
print(spam.upper())
print(spam.lower())
print(spam.islower())
print(spam.isupper())
print(spam.isalpha()) #revisa que haya letras nomas
print(spam.isalnum()) # revisa que haya letras y numeros nomas
print(spam.startswith("h"))
print(spam.endswith("h"))
print(spam.split("o")) #Regresa una lista con los caracteres del split
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
print(spam.strip(" m"))
print(spam.replace("h", "w"))