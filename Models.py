import itertools


class Animal():
    # Incremental ID
    newid = itertools.count()

    def __init__(self, name, breed, birthdate):
        # Incremental ID
        self.id = next(self.newid)
        self. name = name
        self.breed = breed
        self. birthdate = birthdate

    def update(self,name,breed,birthdate):
        self.name = name,
        self.breed = breed
        self.birthdate = birthdate


class Dog(Animal):

    def __init__(self, name, breed, birthdate, father = 0, mother = 0, tame = True):
        super().__init__(name, breed, birthdate)
        self.father = father
        self.mother = mother
        self.tame = tame
    
    
    def serialize(self):
        return {"id": self.id, "name": self.name, "breed": self.breed, "birthdate": self.birthdate, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else "", "tame": self.tame}

    def data_summary(self):
        return {"id": self.id, "name": self.name, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else ""}

    def update(self, name, breed, birthdate, father, mother,tame):
        super().update(name, breed, birthdate)
        self.father = father
        self.mother = mother
        self.tame = tame


class Cat(Animal):

    def __init__(self, name, breed, birthdate, father = 0, mother = 0, sociable = 1):
        super().__init__(name, breed, birthdate)
        self.father = father
        self.mother = mother
        self.sociable = sociable
    
    
    def serialize(self):
        return {"id": self.id, "name": self.name, "breed": self.breed, "birthdate": self.birthdate, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else "", "sociable": self.sociable}

    def data_summary(self):
        return {"id": self.id, "name": self.name, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else ""}


    def update(self, name, breed, birthdate, father, mother,sociable):
        super().update(name, breed, birthdate)
        self.father = father
        self.mother = mother
        self.sociable = sociable

animals = []
