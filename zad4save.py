import pickle
from smartphone import Smartphone

s1 = Smartphone("Apple", "iPhone 13", 799)
s2 = Smartphone("Samsung", "Galaxy S21", 699)
s3 = Smartphone("Google", "Pixel 6", 599)

with open("phones.dat", "wb") as f:
    pickle.dump(s1, f)
    pickle.dump(s2, f)
    pickle.dump(s3, f)

print("Obiekty zostały zapisane do pliku phones.dat.")