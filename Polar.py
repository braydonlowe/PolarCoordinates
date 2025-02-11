import matplotlib.pyplot as plt
import numpy as np

functionsDict = {
	"Add": "+",
	"Subtract": "-",
	"Multiply": "*",
	"Divide": "/",
	"SquareRoot": "sqrt",
	"Exponent": "^",
	"Cos": "cos",
	"Sin": "sin",
	"RightParen": ")",
	"LeftParen": "(",
	}

def updateDigits(string = "10", number = 10, character = ""):
	if string == "10" and number == 10 and character == "":
		string = ''
		number = 0
		return string, number
	else:
		string += character
		number = float(string)
		return string, number
		
		
def updateAlpha(string="10", character=""):
	if string == "10" and character == "":
		string = ''
		return string
	else:
		string += character
		return string


def parsefunction(function):
	#Variables used inside of this frame.
	componentsList = []
	type = ''
	digitString = ''
	alphaString = ''
	digitNumber = 0
	indexCounter = -1
	
	#The for loop is as follows. For each case 1- check type 2-update instances 3-append that thing to that part of the list.
	for character in function:
		if character.isspace() or character == 'y' or character == '=':
			digitString, digitNumber = updateDigits()
			alphaString = updateAlpha()
			continue
			
		elif character.isdigit():
			if type != "digit":
				type = "digit"
				indexCounter += 1
			digitString, digitNumber = updateDigits(digitString, digitNumber, character)
			alphaString = updateAlpha()
			if len(componentsList) <= indexCounter:
				componentsList.append(digitNumber)
			else:
				componentsList[indexCounter] = digitNumber
				
		elif character in functionsDict.values():
			type = "function"
			indexCounter += 1
			digitString, digitNumber = updateDigits()
			alphaString = updateAlpha()
			componentsList.append(character)
			
		elif character.isalpha():
			if type != "alpha":
				type = "alpha"
				indexCounter += 1
			alphaString = updateAlpha(alphaString, character)
			digitString, digitNumber = updateDigits()
			if len(componentsList) <= indexCounter:
				componentsList.append(alphaString)
			else:
				componentsList[indexCounter] = alphaString
			continue
			
	return componentsList
		
def exponential(x, y):
	return x**y

def list_looper(lst, x_value):
	temp = 0
	for i in range(len(lst)):
		#The first two cases handle if it is just a number or our variable x.
		if type(lst[i]) == float:
			temp = lst[i]
			continue
		if lst[i] == 'x':
			return x_value

		#This could potentially run into a problem with the right paren. I need to be able to solve that case in here as well.
		elif lst[i] == 'cos':
			return np.cos(list_looper(lst[i+2:], x_value))
		elif lst[i] == 'sin':
			return np.sin(list_looper(lst[i+2:], x_value))
		elif lst[i] == "*":
			temp *= list_looper(lst[i+1:], x_value)
			return temp
		elif list[i] == "/":
			temp /= list_looper(lst[i+1], x_value)
	return temp
				
				
				

def function_runner(parsed_list, domain):
	range_values = [list_looper(parsed_list, x) for x in domain]
	return range_values
		

def cartesean_polar(angle, length):
	x_list = []
	y_list = []
	for theta in range(len(angle)):
		new_x = length[theta] * np.cos(angle[theta])
		new_y = length[theta] * np.sin(angle[theta])
		x_list.append(new_x)
		y_list.append(new_y)
		
	
	return x_list, y_list
	
def domainList(loopNumber=1, numberOfPieces=1000):
	domain = []
	sizeOfPie = (2 * np.pi) * loopNumber
	for piece in range(numberOfPieces):
		x = sizeOfPie * (piece / numberOfPieces)
		domain.append(x)
	#Need to add the final part of the loop.
	domain.append(sizeOfPie)
	return domain


def main():
	print("Input your function in the format y=<yourFunction>")
	function_input = input("Input: ")
	parsed_list = parsefunction(function_input)
	domain = domainList()
	range_values = function_runner(parsed_list, domain)
	x_values, y_values = cartesean_polar(domain, range_values)
	
	# Plotting lines
	plt.plot(x_values, y_values, label='Line')

	# Adding labels and title
	plt.xlabel('X-axis')
	plt.ylabel('Y-axis')
	plt.title('Polar Coordinates')

	# Adding a legend
	plt.legend()

	# Display the plot
	plt.show()

if __name__ == "__main__":
	main()