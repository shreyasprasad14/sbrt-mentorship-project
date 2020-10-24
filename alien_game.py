import sys

def parse_user_input(user_input):
	if user_input == "help":
		print("load_grid <filename> - Load Grid File")
		print("print_grid - Prints Grid")
	elif user_input == "print_grid":
		print_grid()
	elif "load_grid" in user_input:
		load_grid(user_input.split(" ")[1])
	elif user_input == "exit":
		print("Ending Program")
		sys.exit()
	else:
		print("Could not parse input")

def load_grid(filename):
	print(filename)

def print_grid():
	print(grid)

if __name__ == "__main__":
	grid = []
	print("Welcome! Are you ready to defend Earth?")
	#print("Type load to load a grid file")
	print("Type help to see a list of all commands or enter a command")
	while True:
		print("\nEnter Command:")
		parse_user_input(input())

