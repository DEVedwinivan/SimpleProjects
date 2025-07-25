import random
palabra = [
    "Genial el resultado es {resultado}",
    "El resultado de tu operacion es {resultado}"
    "Notas que buena calculadora, tu resultado {resultado}"
]
while True:
    print(" 1. Suma \n 2. Resta \n 3. División \n 4. Multiplicación \n 5. Salir")
    opcion=int(input("Escribe un valor que aparece de lado de la opción: "))

    if opcion == 5:
        print("Hasta luego")
        break
    elif opcion not in [1, 2, 3 , 4 ,5 ]:
        print("Esa opción no existe, intentalo de nuevo")
        continue

    try:
        valoruno = float(input("Escribe el pimer valor: "))
        valordos = float(input("Escribe el segundo valor: "))
    except ValueError:
        print("Es una calculadora ordinaria, escribe un numero")
        continue

    if opcion == 1:
        print("Suma")
        resultado = valoruno + valordos
    elif opcion == 2:
        print("Resta")
        resultado = valoruno - valordos
    elif opcion == 3:
        print("Division")
        resultado = valoruno / valordos
    elif opcion == 4:
        print("Multiplicación")
        resultado = valoruno * valordos
    frase = random.choice(palabra)
    print(frase.format(resultado=resultado))


# random.choice(frases)