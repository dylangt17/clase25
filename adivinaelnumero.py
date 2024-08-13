from random import randint

def adivina_el_numero():
numero_secreto = randint(0, 20)
intentos =0

print("¡Bienvenido al juego de adivina el numero!")
print("Estoy pensando en un numero entre 1 y 100.¿Puedes adivinar")

while True:  
   intento = int(input("Introduce tu numero!"))   
   intentos = intentos + 1
   distancia=abs(numero_secreto-intento)
   if intento < numero_secreto:
       if distancia<=10:
         print("Demasiado bajo y estas cerca,intenta de nuevo")
        else:
         print("Demasiado bajo y estas lejos,intentan de nuevo.")
     elif    intento > numero_secreto: 
        if distancia<=10:
            print("Demasiado alto y estas cerca. intentan de nuevo")
        else:
            print("Demasiado alto y estas lejos. intenta de nuevo.")    
    else:
     print(f"Felicidades! Adivinaste el numero en (intentos) intentos")
        break         
