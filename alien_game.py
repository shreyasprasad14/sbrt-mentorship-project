import sys, json

class Game():
    def __init__(self):
        self.grid = []
        
    def parse_user_input(self, user_input):
        if user_input == "help":
            print("load_grid <filename> - Load Grid File")
            print("print_grid - Prints Grid")
        elif user_input == "print_grid":
            self.print_grid()
        elif "load_grid" in user_input:
            self.load_grid(user_input.split(" ")[1])
        elif user_input == "save_earth":
            self.start_game()
        elif user_input == "exit":
            print("Ending Program")
            sys.exit()
        else:
            print("Could not parse input")

    def load_grid(self, filename):
        data = json.load(open(filename))
        self.grid = data["Grid"]
        print("\n--------", filename, "loaded--------")

    def print_grid(self):
        print("\n ----------------------------")
        for line in self.grid:
            print("  ", line)
        print("----------------------------")

    def start_game(self):
        if self.grid == []:
            print("You haven't loaded a grid!")
            return

def main():
    print("Welcome! Are you ready to defend Earth?")
    print("Enter a command or type help to see a list of all commands")
    game = Game()
    while True:
        print("\nEnter Command:")
        game.parse_user_input(input())

if __name__ == "__main__":
    main()

