import random

def adivina_num(x):

    print("========================")
    print(" ¡Bienvenidos al Juego!")
    print("========================")
    print("Para ganar, deberás adivinar el número generado por la computadora")

    random_number = random.randint(1, x)  # Número aleatorio entre 1 y x.

    predict = 0

    while predict != random_number:
        predict = int(input(f"Adivina un número entre 1 y {x}: ")) # f-string

        if predict < random_number:
            print("Intenta otra vez. Este número es menor.")
        elif predict > random_number:
            print("Intenta otra vez. Este número es mayor.")
    print(f"¡Felicitaciones! Adivinaste el número {random_number} correctamente.")


adivina_num(100)