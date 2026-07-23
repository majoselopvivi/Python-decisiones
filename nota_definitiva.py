nota = float(input("Ingrese la nota definitiva: "))

print("Su nota es:")

if nota < 3.0:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4.0:
    print("Sobresaliente")
else:
    print("Excelente")