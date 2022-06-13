from Models import Dog

def create_dog():
    dogs = []
    name = str(input("Introduzca nombre del perro: "))
    breed = str(input("Introduzca raza del perro: "))
    birthdate = str(input("Introduzca fecha de nacimiento: "))
    father_id = int(
        input("Introduzca identificador del padre, si no lo conoce introduzca 0: "))
    mother_id = int(
        input("Introduzca identificador de la madre,si no lo conoce introduzca 0: "))
    dog = Dog(name, breed, birthdate, father_id, mother_id)
    dogs.append(dog)


def start():
    user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para ...
    -Introduzca 3 para  
    -Introduzca 4 para ...
    -Pulsa ENTER sino quiere hacer nada 
    """)

    while user_choice != "":

        if user_choice == "1":
            create_dog()

        user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para ...
    -Introduzca 3 para ...
    -Introduzca 4 para ...
    -Pulsa ENTER sino quiere hacer nada 
    """)


if __name__ == "__main__":
    start()
