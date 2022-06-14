from Models import Dog, dogs

def create_dog():
    name = str(input("Introduzca nombre del perro: "))
    breed = str(input("Introduzca raza del perro: "))
    birthdate = str(input("Introduzca fecha de nacimiento: "))
    father_id = int(
        input("Introduzca identificador del padre, si no lo conoce introduzca 0: "))
    mother_id = int(
        input("Introduzca identificador de la madre,si no lo conoce introduzca 0: "))
    dog = Dog(name, breed, birthdate, father_id, mother_id)
    dogs.append(dog)

def show_all_dogs():
    return [dog.data_summary() for dog in dogs]

def get_single_dog():
    dog_id = int(input("Introduzca el identificador del perro que desea ver: "))
    dog_found = [dog for dog in dogs if dog.id == dog_id]

    return dog_found[0].serialize()


def start():
    user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para mostrar listado perros registrados
    -Introduzca 3 para ver datos de un perro
    -Introduzca 4 para ...
    -Pulsa ENTER sino quiere hacer nada 
    """)

    while user_choice != "":

        if user_choice == "1":
            create_dog()

        if user_choice == "2":
            print(show_all_dogs())

        if user_choice == "3":
            print(get_single_dog())

        user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para mostrar listado perros registrados
    -Introduzca 3 para ver datos de un perro
    -Introduzca 4 para ...
    -Pulsa ENTER sino quiere hacer nada 
    """)


if __name__ == "__main__":
    start()
