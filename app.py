from Models import Dog, Cat,animals

def create_dog():
    name = str(input("Introduzca nombre del perro: "))
    breed = str(input("Introduzca raza del perro: "))
    birthdate = str(input("Introduzca fecha de nacimiento: "))
    father_id = int(
        input("Introduzca identificador del padre, si no lo conoce introduzca 0: "))
    mother_id = int(
        input("Introduzca identificador de la madre,si no lo conoce introduzca 0: "))
    tame = input(
        "Introduzca True si el perro está entrenado, False en caso contrario: ")
    dog = Dog(name, breed, birthdate, father_id, mother_id, tame)
    animals.append(dog)

def update_dog():
    dog_id = int(
        input("Introduzca el identificador del perro que desea modificar: "))
    dog_found = [dog for dog in animals if dog.id == dog_id]
    dog_found[0].name = str(input("Introduzca nombre del perro: "))
    dog_found[0].breed = str(input("Introduzca raza del perro: "))
    dog_found[0].birthdate = str(input("Introduzca fecha de nacimiento: "))
    dog_found[0].father = int(
        input("Introduzca identificador del padre, si no lo conoce introduzca 0: "))
    dog_found[0].mother = int(
        input("Introduzca identificador de la madre,si no lo conoce introduzca 0: "))
    dog_found[0].tame = input(
        "Introduzca True si el perro está entrenado, False en caso contrario: ")

def create_cat():
    name = str(input("Introduzca nombre del gato: "))
    breed = str(input("Introduzca raza del gato: "))
    birthdate = str(input("Introduzca fecha de nacimiento: "))
    father_id = int(
        input("Introduzca identificador del padre, si no lo conoce introduzca 0: "))
    mother_id = int(
        input("Introduzca identificador de la madre,si no lo conoce introduzca 0: "))
    sociable = int(input(
        "Introduzca un número del 1-5. 1 es «muy poco sociable» y 5 es «muy sociable»: "))
    cat = Cat(name, breed, birthdate, father_id, mother_id, sociable)
    animals.append(cat)


def show_all_animals():
    return [animal.data_summary() for animal in animals]


def get_single_animal():
    animal_id = int(
        input("Introduzca el identificador del animal que desea ver: "))
    animal_found = [animal for animal in animals if animal.id == animal_id]

    return animal_found[0].serialize()


def start():
    user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para mostrar listado animales registrados
    -Introduzca 3 para ver datos de un animal
    -Introduzca 4 para modificar datos de un perro
    Introduzca 5 para crear un nuevo registro de un gato
    -Pulsa ENTER sino quiere hacer nada 
    """)

    while user_choice != "":

        if user_choice == "1":
            create_dog()

        if user_choice == "2":
            print(show_all_animals())

        if user_choice == "3":
            print(get_single_animal())

        if user_choice == "4":
            update_dog()

        if user_choice == "5":
            create_cat()

        user_choice = input("""¿Qué desea hacer?:
    -Introduzca 1 para crear un nuevo registro de un perro
    -Introduzca 2 para mostrar listado animales registrados
    -Introduzca 3 para ver datos de un animal
    -Introduzca 4 para para modificar datos de un perro
    -Introduzca 5 para crear un nuevo registro de un gato
    -Pulsa ENTER sino quiere hacer nada 
    """)


if __name__ == "__main__":
    start()
