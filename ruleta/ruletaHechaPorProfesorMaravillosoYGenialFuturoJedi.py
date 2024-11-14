import time
import os
import random



# inicializar participantes
participante1 = input("Dime el nombre del primer participante: ")
participante2 = input("Dime el nombre del segundo participante: ")
participante3 = input("Dime el nombre del tercer participante: ")
jugadores = [participante1, participante2, participante3]
puntuaciones_jugadores = [0,0,0]
comodines_jugadores = [0,0,0]


vocales = ["a", "e", "i", "o", "u"]
palabras = ["basket es lo mejor","que me entierren con la picha por fuera"]
palabra_secreta : str= random.choice(palabras)
palabra_a_mostrar_con_guiones = []
for letra in palabra_secreta:
    if letra == " ":
        palabra_a_mostrar_con_guiones.append(" ")
    else:
        palabra_a_mostrar_con_guiones.append("_")

ruleta_valores = [100, 200, 300, 400, 500, 600, 700, 800, 900, "Pierde turno", "Quiebra","Comodin"]
indice_ruleta: int = 0


def __limpiar_pantalla():
    # Limpiar la pantalla para que la animación sea visible
    if os.name == 'nt':  # Si es Windows
        os.system('cls')
    else:  # Si es Linux o Mac
        os.system('clear')




def girar_ruleta(fuerza_jugador):
    global indice_ruleta
    resultado = 0
    fuerza_jugador += 1
    print("¡Girando la ruleta!")
    for i in range(fuerza_jugador):  # Simular múltiples vueltas
        indice_ruleta = (indice_ruleta+i) % len(ruleta_valores)
        resultado = ruleta_valores[indice_ruleta]
        __limpiar_pantalla()  # Limpiar pantalla en cada iteración
        print(f"--> {resultado} <--")  # Mostrar valor temporal
        time.sleep(0.1)  # Pausa breve para animación

   
    return resultado

cambia_turno : bool = False
turno : int = 0 

while '_' in palabra_a_mostrar_con_guiones:
    if cambia_turno:
        turno = (turno + 1) % 3
        cambia_turno = False
    jugador = jugadores[turno]
    print("\nTurno de", jugador, ". Puntuación actual:", puntuaciones_jugadores[turno])
    
    fuerza = int(input("Dime la fuerza con la que quieres tirar: "))
    # Girar la ruleta y obtener el resultado
    resultado_ruleta = girar_ruleta(fuerza)
    print("Resultado de la ruleta: -->", resultado_ruleta, "<--")

    # quiebra , pierdeturno, dime letra
    if resultado_ruleta == "Quiebra" or resultado_ruleta == "Pierde turno":
        cambia_turno = True
        if (resultado_ruleta == "Quiebra"):
            puntuaciones_jugadores[turno] = 0
    else:
        #Pedir letra
        letra = input("Dime una letra: ")
        #entrada invalida
        if letra in vocales or len(letra) != 1 or letra in palabra_a_mostrar_con_guiones:
            cambia_turno = True
            print("Entrada invalida")
            continue
        else:
            #Letra correcta
            if not letra in palabra_secreta:
                print("La letra no esta en la palabra")
                cambia_turno = True
                continue
            elif letra in palabra_secreta:
                print(f"La letra {letra} esta en la palabra.")
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i] == letra:
                        palabra_a_mostrar_con_guiones[i] = letra
                num_letras = palabra_secreta.count(letra)
                if (resultado_ruleta == "Comodin"):
                    comodines_jugadores[turno] += 1
                    continue
                else:
                    puntuaciones_jugadores[turno] += num_letras * resultado_ruleta
                    print(" ".join(palabra_a_mostrar_con_guiones))
                    
                    seguir_tirando :bool = False
                    while not seguir_tirando:
                        respuesta = input("Quieres Comprar/resolver/tirar?: ")
                        if respuesta.lower == "comprar":
                            if puntuaciones_jugadores[turno] < 50:
                                print("No tienes suficiente dinero")
                                cambia_turno = True
                                seguir_tirando = True
                            else:
                                puntuaciones_jugadores[turno] -= 50
                                vocal = input("Dime una vocal: ")
                                if vocal not in vocales or vocal in palabra_a_mostrar_con_guiones:
                                    print("Por tonto para turno, entrada incorrecta")
                                    cambia_turno = True
                                    seguir_tirando = True
                                else:
                                    for i in range(len(palabra_secreta)):
                                        if palabra_secreta[i] == vocal:
                                            palabra_a_mostrar_con_guiones[i] = vocal
                        elif respuesta.lower == "resolver":
                            intento_palabra : str = input("Dime la palabra: ")
                            if intento_palabra == palabra_secreta:
                                print("Has ganado")
                                palabra_a_mostrar_con_guiones = palabra_secreta
                            else:
                                print("Has perdido")
                                cambia_turno = True
                                seguir_tirando = True
                        

            
