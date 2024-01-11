import pickle
from smartphone import Smartphone

with open("phones.dat", "rb") as f:
    while True:
        try:
            s = pickle.load(f)
            print(s)
        except EOFError:
            break

print("Obiekty zostały odczytane z pliku phones.dat.")