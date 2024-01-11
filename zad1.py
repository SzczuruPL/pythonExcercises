import random


class Coin:
    def __init__(self):
        if random.randint(0, 1) == 0:
            self.side = "Orzeł"
        else:
            self.side = "Reszka"

    def throw(self):
        if random.randint(0, 1) == 0:
            self.side = "Orzeł"
        else:
            self.side = "Reszka"

    def __str__(self):
        return self.side

class Game:
    def __init__(self):
        self.coins = [Coin(), Coin(), Coin()]
        self.balance = 0

    def play(self):
        for coin in self.coins:
            coin.throw()
            if coin.side == 'Heads':
                if coin is self.coins[0]:
                    self.balance += 1
                elif coin is self.coins[1]:
                    self.balance += 2
                else:
                    self.balance += 5

        if self.balance >= 20:
            return True
        else:
            return False

coin1 = Coin()
coin2 = Coin()
coin3 = Coin()

print(coin1)
coin1.throw()
print(coin1)

print(coin2)
coin2.throw()
print(coin2)

print(coin3)
coin3.throw()
print(coin3)

wins = 0
losses = 0

for i in range(100):
    game = Game()
    while True:
        if game.play():
            wins += 1
            break
        elif game.balance >= 20:
            losses += 1
            break

print("Wins:", wins)
print("Losses:", losses)