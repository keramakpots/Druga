
import pickle

class Manager:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

jurek = Manager("Jurek", "Piastuch")

print(jurek.name)
data = jurek

PIK = "pickle.dat"

with open(PIK, "wb") as f:
    pickle.dump(data, f)

with open(PIK, "rb") as f:
    loaded = pickle.load(f)

print(vars(loaded))
