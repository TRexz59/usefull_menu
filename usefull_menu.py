#   Es un menu con varias opciones utiles. (Hecho como poryecto de principiante)

while True:                                                                         # Bucle infinito para el menu
    try:
        print("\t--- MENU DE OPCIONES ---")
        print("""
    1. Conversor de Euros a USD
    2. Juego de adivinar el número (1-20)
    3. Comprobar si un número es par o impar
    4. Salir del programa
        """)
                                                                                    
        opc = input("Elige una opcion del menu (1-4): ")                            # Menu de opciones

        if int(opc) < 1 or int(opc) > 4:
            print("Opcion no valida, elige entre 1 y 4")
        
        elif opc == "1":                                                            # Conversor de Euros a USD
            try:
                euros = float(input("· Introduce la cantidad de euros: "))
                usd = euros * 1.16
                print("%f euros son %f USD" % (euros, usd))
            except ValueError:
                print("Introduce una cantidad válida de saldo")

        elif opc == "2":                                                            # Juego de adivinar el número (1-20)
            import random
            num_ale = random.randint(1,20)
            intentos = 0

            while intentos < 5:
                try:    
                    num_user = int(input("· Adivina el número entre 1 y 20: "))
                    if num_user < 1 or num_user > 20:
                        print("Introduce un número dentro del rango (1-20)")
                        print("Por listillo te quito un intento")
                        intentos = intentos + 1                
                    elif num_user == num_ale:
                        print("!Has Ganado¡")
                        break
                    elif num_user > num_ale:
                        print("Mas bajo")
                        intentos = intentos + 1
                    elif num_user < num_ale:
                        print("Mas alto")
                        intentos = intentos + 1            
                except ValueError:
                    print("Eso no es un número válido")

            print("El número era: %d" % (num_ale))

        elif opc == "3":                                                            # Comprobar si un número es par o impar                 
            try:
                print("· Comprueba si un número es par o impar")
                num = float(input("Introduce el número: "))
                if num % 2 == 0:
                    print("El número %d es par" % num)
                else:
                    print("El número %d es impar" % num)
            except ValueError:
                print("Introduce un número válido")

        elif opc == "4":                                                            # Salir del programa
            print("¡Gracias por usar mi programa, hasta luego!")
            break
    
    except ValueError:
        print("Introduce una opción válida para usar el programa")