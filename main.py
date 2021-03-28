from Objets.game import Game


def input_size():
    try:
        entered_size = int(input("Enter board entered_size : "))
        return entered_size
    except ValueError:
        print("Make sure to enter a whole number")

    return input_size()


size = input_size()
game = Game(size)
game.play()
