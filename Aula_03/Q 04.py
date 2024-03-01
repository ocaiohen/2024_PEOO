base = float(input("Insira a base do retângulo: "))
altura = float(input("Insira a altura do retângulo: "))

area, perimetro, diagonal = base * altura, 2 * base + 2 * altura, ((base ** 2 + altura ** 2)**(1/2))

print(f"Área: {area:.2f}; Perímetro: {perimetro:.2f}; Diagonal: {diagonal:.2f}")