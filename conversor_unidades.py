#Conversor de medidas
#Conversor de medidas comunes (Longitudes, Peso, Temperatura)

while True: 
    print ("========================================\nBienvendio al conversor de unidades \n¿Qué categoría te interesa?\n========================================")

    print("1. Longitud (Cm, Mt, Km)")
    print("2. Peso (Kg, gramo, etc.)")
    print("3. Temperatura (Celsius, Fahrenheit, Kelvin)")
    print("4. Cerrar el conversor")
    cat = int(input("Escribe el valor de la opción que te interesa: "))

    if cat == 4:
        print("Hasta pronto.")
        break
    if cat not in [1,2,3,4]:
        print("Esa categoría no extiste 😔")
        continue
    if cat == 1:
        while True:
            print("Bienvenido a longitud 📏\nElige una opción:")
            print("1. Centimetro \n2. Metro \n3. Kilometro \n4. Elegir otra categoría")
            opcion = int(input("Opción: "))
            if opcion == 4:
                print("Bye 👋")
                break
            if opcion not in [1, 2, 3, 4]:
                print("Esa opción no existe 🤷")
                continue
            try:
                valor = float(input("Escribe un valor: "))
            except ValueError:
                print("Eso no es un numero 😅")
                continue
            if opcion == 1:
                primero = valor * 0.01
                segundo = valor * 0.00001
                resultado = f"{primero}Mt y {segundo}Km"
            if opcion == 2:
                primero = valor * 100
                segundo = valor * 0.001
                resultado = f"{primero}Cm y {segundo}Km"
            if opcion == 3:
                primero = valor * 100000
                segundo = valor * 1000
                resultado = f"{primero}Cm y {segundo}Mt"

            print(f"Los resultados son {resultado}")
    if cat == 2:
        while True:
            print("Bienvendio a Peso ⚖️\nElige una opción:")
            print("1. Kilogramo \n2. Gramo \n3. Onza \n4. Tonelada \n 5. Elegir otra categoria")
            opcion = int(input("Opción: "))
            if opcion == 5:
                print("Hasta la proxima👋")
                break
            if opcion not in[1, 2, 3, 4, 5]:
                print("Esa opción no existe 🤷")
                continue
            try:
                valor = float(input("Escribe un valor: "))
            except ValueError:
                print("Ese no es un valor valido 😅")
                continue
            if opcion == 1:
                primero = valor * 1000 
                segundo = valor * 35.273962
                tercero = valor * 0.001
                resultado = f"{primero}G, {segundo}oz, {tercero}t"
            if opcion == 2:
                primero = valor * 0.001 
                segundo = valor * 0.03527396
                tercero = valor * 0.000001
                resultado = f"{primero}Kg, {segundo}oz, {tercero}t"
            if opcion == 3:
                primero = valor * 0.02834952
                segundo = valor * 28.3495231
                tercero = valor * 0.00002835
                resultado = f"{primero}Kg, {segundo}G, {tercero}t"
            if opcion == 4:
                primero = valor * 1000
                segundo = valor * 1000000
                tercero = valor * 35273.962
                resultado = f"{primero}Kg, {segundo}G, {tercero}oz"
            print(F"Los resultados de esta conversión son: {resultado}")
    if cat == 3:
            while True:
                print("Bienvenido a Temperatura 🌡️\nElige una opción:")
                print("1. Celsius \n2. Farenheit \n3. Kelvin \n4. Elegir otra categoría")
                opcion = int(input("Opción: "))
                if opcion == 4:
                    print("Nos vemos ^_^")
                    break
                if opcion not in[1,2,3,4]:
                    print("Esa opción no aparece en el registro, intentalo de nuevo por favor. ◑﹏◐")
                    continue
                try:
                    valor = float(input("Escribe un valor valido: "))
                except ValueError:
                    print("Ese no es un valor valido 🤨")
                    continue
                if opcion == 1:
                    primero = (valor * 9/5) + 32
                    segundo = valor + 273.15
                    resultado = f"los resultados de la conversion de temperaturas es:{primero}F y {segundo}K"
                if opcion == 2:
                    primero = (valor - 32) * 5/9
                    segundo = (valor + 459.67) * 5/9
                    resultado = f"los resultados de la conversion de temperaturas es:{primero}C y {segundo}K"
                if opcion == 3:
                    primero = valor - 273.15
                    segundo = (valor * 9/5) - 459.67
                    resultado = f"los resultados de la conversion de temperaturas es:{primero}C y {segundo}F"
                print (resultado)