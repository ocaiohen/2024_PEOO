nome = input("Digite seu nome completo: ").strip()
primeiroNome = ""
for i in range(len(nome)):
    if nome[i] == " ":
        primeiroNome = nome[:i]
        break
print(f"Bem-vindo ao Python, {primeiroNome}")

# ou um método mais simples

# nome = input("Digite seu nome completo: ").strip()
# primeiroNome = nome[:nome.index(" ")]
# print(f"Bem-vindo ao Python, {primeiroNome}")