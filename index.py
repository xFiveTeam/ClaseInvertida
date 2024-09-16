# Inicio del juego Mario Bros rescatando a la princesa
def print_banner(message, symbol="=", width=40):
    print("\n" + symbol * width)
    print(" " * 10 + message)
    print(symbol * width + "\n")

def get_valid_input(prompt, valid_option1, valid_option2):
    try:
        response = input(prompt)
        while response != valid_option1 and response != valid_option2:
            print("\nSelección inválida, vuelve a intentarlo")
            response = input(prompt)
        return response
    except Exception as e:
        print("Error: ", e)
        return None

def select_character():
    try:
        print("\nSelecciona tu personaje\n1. Mario\n2. Luigi")
        character = input("\nEl Personaje Seleccionado es: \n> ")
        while character != "1" and character != "2":
            print("\nSelección inválida, vuelve a intentarlo")
            character = input("\nEl Personaje Seleccionado es: \n> ")
        return character 
    except Exception as e:
        print(f"Error: ", e)
        return None

def select_world():
    try:
        print("\nSelecciona tu mundo\n1. Alice\n2. Marta")
        world = input("\nEl Mundo Seleccionado es: \n> ")
        while world != "1" and world != "2":
            print("\nSelección inválida, vuelve a intentarlo")
            world = input("\nEl Mundo Seleccionado es: \n> ")
        return "Alice" if world == "1" else "Marta" 
    except Exception as e:
        print(f"Error: ", e)
        return None

def display_lives(lifes):
    try:
        if lifes > 0:
            print_banner("Tienes " + str(lifes) + " vidas", "*")
        else:
            print_banner("Has perdido todas tus vidas\nGAME OVER", "*")
    except Exception as e:
        print(f"Error: ", e)

def play_level(level, lifes, world):
    try:
        decision = get_valid_input("\nNivel " + str(level) + ": Selecciona el rumbo (izquierda/derecha): \n> ", "izquierda", "derecha")
        if (decision == "izquierda" and world == "Alice") or (decision == "derecha" and world == "Marta"):
            print_banner("Has seleccionado el camino correcto, sigamos adelante", "-")
        else:
            print_banner("Has seleccionado el camino incorrecto, has perdido una vida", "-")
            lifes -= 1
            display_lives(lifes)
        return lifes
    except Exception as e:
        print(f"Error: ", e)
        return lifes

def start():
    try:
        print_banner("Bienvenido a Mario Bros")
        lifes = 3

        respuesta = get_valid_input("\nDesea jugar? (si/no): \n> ", "si", "no")

        if respuesta == "si":
            print_banner("Comencemos a jugar")
            character = select_character()
            world = select_world()

            print_banner("Comienza el juego con" + character + ", recuerda que tienes 3 vidas, donde cada decisión que tomes puede cambiar el rumbo de tu juego\nRescata a la Princesa Peach del castillo de Bowser\nBuena Suerte")

            for level in range(1, 5):
                lifes = play_level(level, lifes, world)
                if lifes <= 0:
                    break

            if lifes > 0:
                decision = get_valid_input("\nNivel Final: Selecciona el rumbo (izquierda/derecha): \n> ", "izquierda", "derecha")
                if (decision == "izquierda" and world == "Alice") or (decision == "derecha" and world == "Marta"):
                    print_banner("Felicidades, has rescatado a la princesa Peach")
                else:
                    print_banner("Has seleccionado el camino incorrecto, has perdido al amor de tu vida, la princesa Peach\nGAME OVER")
    except Exception as e:
        print(f"Error: ", e)

start()