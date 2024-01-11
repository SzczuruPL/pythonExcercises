class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalpha() or len(value) < 3:
            raise ValueError('Name should be at least 3 letters long and contain only letters')
        self._name = value

    @property
    def mood(self):
        mood_sum = self.hunger + self.tiredness
        if mood_sum < 5:
            return 'happy'
        elif mood_sum < 11:
            return 'satisfied'
        elif mood_sum < 16:
            return 'nervous'
        else:
            return 'angry'

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    def talk(self):
        self._passage_of_time()
        print(f"{self.name} is {self.mood}.")

    def eat(self, food=4):
        self._passage_of_time()
        self.hunger -= food

    def play(self, fun=4):
        self._passage_of_time()
        self.tiredness -= fun

    def __str__(self):
        return f"{self.name} is {self.mood}, hunger level: {self.hunger}, tiredness level: {self.tiredness}"


def main():
    pet_name = input("What will you name your pet? ")
    pet = Pet(pet_name)

    while True:
        print()
        print("What would you like to do?")
        print("1. Check on your pet")
        print("2. Feed your pet")
        print("3. Play with your pet")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(pet)
        elif choice == '2':
            food = int(input("How much food would you like to give your pet? "))
            pet.eat(food)
        elif choice == '3':
            fun = int(input("How long would you like to play with your pet? "))
            pet.play(fun)
        elif choice == '4':
            print("Goodbye!")
            break
        elif choice == 'xy':
            print(pet)
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()