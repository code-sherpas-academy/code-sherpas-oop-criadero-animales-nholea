import itertools

class Dog():
    # Incremental ID
    newid = itertools.count()

    def __init__(self, name, breed, birthdate, father=0, mother=0):
        # Incremental ID
        self.id = next(self.newid)
        self. name = name
        self.breed = breed
        self. birthdate = birthdate
        self.father = father
        self.mother = mother

    def serialize(self):
        return {"id": self.id, "name": self.name, "breed": self.breed, "birthdate": self.birthdate, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else ""}

    def data_summary(self):
        return {"id": self.id, "name": self.name, "father": self.father if self.father > 0 else "", "mother": self.mother if self.mother > 0 else ""}

dogs = []