from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Inicio del juego Mario Bros rescatando a la princesa

print(Fore.GREEN + "Bienvenido a Mario Bros")

# Preguntar al usuario si desea jugar

respuesta = input(Fore.YELLOW + "Desea jugar? (si/no): ")

def personaje_seleccionado(personaje):
    if personaje == "Mario":
        print(Fore.BLUE + "Seleccionaste a Mario")
    elif personaje == "Luigi":
        print(Fore.BLUE + "Seleccionaste a Luigi")
    else:
        print(Fore.RED + "Selección inválida")
        
def mundo_seleccionado(mundo):
    if mundo == "Alice":
        print(Fore.BLUE + "Seleccionaste el mundo Alice")
    elif mundo == "Marta":
        print(Fore.BLUE + "Seleccionaste el mundo Marta")
    else:
        print(Fore.RED + "Selección inválida")
        
def vidas(vida):
    if vida == 3:
        print(Fore.GREEN + "Tienes 3 vidas")
    elif vida == 2:
        print(Fore.YELLOW + "Tienes 2 vidas")
    elif vida == 1:
        print(Fore.RED + "Tienes 1 vida")
    else:
        print(Fore.RED + "Has perdido todas tus vidas")
        print(Fore.RED + "GAME OVER")

def level1(vida, mundo):
    decision = input(Fore.YELLOW + "Nivel 1: Selecciona el rumbo (izquierda/derecha): ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print(Fore.GREEN + "Has seleccionado el camino correcto, sigamos adelante")
        level2(vida, mundo)
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print(Fore.RED + "Has seleccionado el camino incorrecto, has perdido una vida")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level1(vida, mundo)

def level2(vida, mundo):
    decision = input(Fore.YELLOW + "Nivel 2: Selecciona el rumbo (izquierda/derecha): ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print(Fore.GREEN + "Has seleccionado el camino correcto, sigamos adelante")
        level3(vida, mundo)
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print(Fore.RED + "Has seleccionado el camino incorrecto, has perdido una vida")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level2(vida, mundo)

def level3(vida, mundo):
    decision = input(Fore.YELLOW + "Nivel 3: Selecciona el rumbo (izquierda/derecha): ")
    if (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print(Fore.GREEN + "Has seleccionado el camino correcto, sigamos adelante")
        level4(vida, mundo)
    elif (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print(Fore.RED + "Has seleccionado el camino incorrecto, has perdido una vida")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level3(vida, mundo)

def level4(vida, mundo):
    decision = input(Fore.YELLOW + "Nivel 4: Selecciona el rumbo (izquierda/derecha): ")
    if (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print(Fore.GREEN + "Has seleccionado el camino correcto, sigamos adelante")
        final_level(vida, mundo)
    elif (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print(Fore.RED + "Has seleccionado el camino incorrecto, has perdido una vida")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level4(vida, mundo)

def final_level(vida, mundo):
    decision = input(Fore.YELLOW + "Nivel Final: Selecciona el rumbo (izquierda/derecha): ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print(Fore.GREEN + "Felicitades, has rescatado a la princesa Peach")
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print(Fore.RED + "Has seleccionado el camino incorrecto, has perdido al amor de tu vida, la princesa Peach")
        print(Fore.RED + "GAME OVER")

if respuesta == "si":
    print(Fore.GREEN + "Comencemos a jugar")
    print(Fore.CYAN + "Selecciona tu personaje")
    print(Fore.CYAN + "1. Mario")
    print(Fore.CYAN + "2. Luigi")

    personaje = input(Fore.YELLOW + "El Personaje Seleccionado es: ")
    personaje_seleccionado(personaje)

    print(Fore.CYAN + "Selecciona tu mundo")
    print(Fore.CYAN + "Alice")
    print(Fore.CYAN + "Marta")
    mundo = input(Fore.YELLOW + "El Mundo Seleccionado es: ")
    mundo_seleccionado(mundo)

    print(Fore.GREEN + "Comenzando el juego, recuerda que tienes 3 vidas, donde cada decisión que tomes puede cambiar el rumbo de tu juego")
    print(Fore.GREEN + "Rescata a la Princesa Peach del castillo de Bowser")
    print(Fore.GREEN + "Buena Suerte", personaje)

    vida = 3

    # Iniciar el juego desde el nivel 1
    level1(vida, mundo)