import random

class Die:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = None

    def roll(self):
        self.__value = random.randint(1, self.__sides)

    def get_sides(self):
        return self.__sides

    def get_value(self):
        return self.__value

    def __str__(self):
        return f"Number of sides: {self.__sides}\nValue: {self.__value}"


def play_game():
    player_score = 0
    computer_score = random.randint(1, 21)

    while True:
        input("Press Enter to roll the dice.")
        player_dice_1 = Die(6)
        player_dice_2 = Die(6)

        player_dice_1.roll()
        player_dice_2.roll()

        player_score += player_dice_1.get_value() + player_dice_2.get_value()
        print(f"Your dice rolls: {player_dice_1.get_value()}, {player_dice_2.get_value()}")
        print(f"Your current score: {player_score}")

        if player_score > 21:
            print("Bust! You lost.")
            break

        choice = input("Do you want to roll again? (y/n) ")
        if choice.lower() == 'n':
            break

    print(f"\nComputer's score: {computer_score}")
    if player_score <= 21 and (player_score > computer_score or computer_score > 21):
        print("You won!")
    else:
        print("You lost.")


if __name__ == "__main__":
    play_game()