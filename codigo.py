def calculadora():
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1/2/3/4/5): ")

        if opcion == '5':
            break

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Ingresa números válidos.")
                continue

            if opcion == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: No se puede dividir por cero.")
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

calculadora()