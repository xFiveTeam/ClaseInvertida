# Inicio del juego Mario Bros rescatando a la princesa

print("\n" + "="*40)
print(" " * 10 + "Bienvenido a Mario Bros")
print("="*40 + "\n")

# Preguntar al usuario si desea jugar

respuesta = input("\nDesea jugar? (si/no): \n> ")

def personaje_seleccionado(personaje):
    if personaje == "Mario":
        print("\n" + "-"*40)
        print(" " * 10 + "Seleccionaste a Mario")
        print("-"*40 + "\n")

    elif personaje == "Luigi":
        print("\n" + "-"*40)
        print(" " * 10 + "Seleccionaste a Luigi")
        print("-"*40 + "\n")

    else:
        print("\n" + "-"*40)
        print(" " * 10 + "Selección inválida")
        print("-"*40 + "\n")
 
        
def mundo_seleccionado(mundo):
    if mundo == "Alice":
        print("\n" + "-"*40)
        print(" " * 10 + "Seleccionaste el mundo Alice")
        print("-"*40 + "\n")
   
    elif mundo == "Marta":
        print("\n" + "-"*40)
        print(" " * 10 + "Seleccionaste el mundo Marta")
        print("-"*40 + "\n")

    else:
        print("\n" + "-"*40)
        print(" " * 10 + "Selección inválida")
        print("-"*40 + "\n")

        
def vidas(vida):
    if vida == 3:
        print("\n" + "*"*40)
        print(" " * 10 + "Tienes 3 vidas")
        print("*"*40 + "\n")
    elif vida == 2:
        print("\n" + "*"*40)
        print(" " * 10 + "Tienes 2 vidas")
        print("*"*40 + "\n")
    elif vida == 1:
        print("\n" + "*"*40)
        print(" " * 10 + "Tienes 1 vida")
        print("*"*40 + "\n")
    else:
        print("\n" + "*"*40)
        print(" " * 10 + "Has perdido todas tus vidas")
        print(" " * 10 + "GAME OVER")
        print("*"*40 + "\n")

def level1(vida, mundo):
    decision = input("\nNivel 1: Selecciona el rumbo (izquierda/derecha): \n> ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino correcto, sigamos adelante")
        print("-"*40 + "\n")
        level2(vida, mundo)
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino incorrecto, has perdido una vida")
        print("-"*40 + "\n")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level1(vida, mundo)

def level2(vida, mundo):
    decision = input("\nNivel 2: Selecciona el rumbo (izquierda/derecha): \n> ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino correcto, sigamos adelante")
        print("-"*40 + "\n")
        level3(vida, mundo)
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino incorrecto, has perdido una vida")
        print("-"*40 + "\n")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level2(vida, mundo)

def level3(vida, mundo):
    decision = input("\nNivel 3: Selecciona el rumbo (izquierda/derecha): \n> ")
    if (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino correcto, sigamos adelante")
        print("-"*40 + "\n")
        level4(vida, mundo)
    elif (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino incorrecto, has perdido una vida")
        print("-"*40 + "\n")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level3(vida, mundo)

def level4(vida, mundo):
    decision = input("\nNivel 4: Selecciona el rumbo (izquierda/derecha): \n> ")
    if (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino correcto, sigamos adelante")
        print("-"*40 + "\n")
        final_level(vida, mundo)
    elif (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print("\n" + "-"*40)
        print(" " * 10 + "Has seleccionado el camino incorrecto, has perdido una vida")
        print("-"*40 + "\n")
        vida -= 1
        vidas(vida)
        if vida > 0:
            level4(vida, mundo)

def final_level(vida, mundo):
    vida = vida
    decision = input("\nNivel Final: Selecciona el rumbo (izquierda/derecha): \n> ")
    if (decision == "izquierda" and mundo == "Alice") or (decision == "derecha" and mundo == "Marta"):
        print("\n" + "="*40)
        print(" " * 10 + "Felicitades, has rescatado a la princesa Peach")
        print("="*40 + "\n")
    elif (decision == "derecha" and mundo == "Alice") or (decision == "izquierda" and mundo == "Marta"):
        print("\n" + "="*40)
        print(" " * 10 + "Has seleccionado el camino incorrecto, has perdido al amor de tu vida, la princesa Peach")
        print(" " * 10 + "GAME OVER")
        print("="*40 + "\n")

if respuesta == "si":
    print("\n" + "="*40)
    print(" " * 10 + "Comencemos a jugar")
    print("="*40 + "\n")

    # Selección de personaje
    personaje = input("\nSelecciona tu personaje (Mario/Luigi): \n> ")
    if personaje_seleccionado(personaje):
        
        # Selección de mundo
        mundo = input("\nSelecciona tu mundo (Alice/Marta): \n> ")
        if mundo_seleccionado(mundo):

            # Inicio del juego
            print("\n" + "="*40)
            print(" " * 10 + "Comienza el juego, recuerda que tienes 3 vidas, donde cada decisión que tomes puede cambiar el rumbo de tu juego")
            print(" " * 10 + "Rescata a la Princesa Peach del castillo de Bowser")
            print(" " * 10 + "Buena Suerte,", personaje)
            print("="*40 + "\n")

            vida = 3

            # Iniciar el juego desde el nivel 1
            level1(vida, mundo)
        else:
            print("Selección de mundo inválida. Fin del juego.")
    else:
        print("Selección de personaje inválida. Fin del juego.")
else:
    print("\n" + "="*40)
    print(" " * 10 + "Hasta la próxima")
    print("="*40 + "\n")