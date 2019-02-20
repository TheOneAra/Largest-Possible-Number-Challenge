  # Give the user instructions.
print("Type a single number, and then press enter. Type that you are done once you have typed the amount of numbers you want to sort.")

  # Ask the user to input a single number.
nmbr = input("Type a number: ")

  # Add the user inputed number to listNmbr.
listNmbr = []
listNmbr.append(nmbr)

  # While the user input is a number, add the user inputed number to listNmbr.
while nmbr.isnumeric():
	nmbr = input("Type a number: ")
	listNmbr.append(nmbr)

  # If the user input is not a number, print the list in correct order and end the program.
else:
	listNmbr.sort()
	listNmbr.reverse()
	if nmbr.isalpha:
		listNmbr.remove(nmbr)
	print("The largest possible number is: ")
	for numbers in listNmbr:
		print (numbers, end = "")
	input("\nProgram complete! Press ENTER to exit.")