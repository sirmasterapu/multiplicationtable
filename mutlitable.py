
def multi_table(start, end):
	'''Creates a multiplication table of given numbers'''
	list = []
	output = '    '#Gets the indent to make the list look nice

	for number in range(start, end+1):
		subList = [str(number) + '|']#Builds the original number range on the left side
		output += '  ' + str(number) + ' '#Builds the top of of the table
		
		for num2 in range(start, end+1):#Multiplies one number by the other numbers asked for
			multiply = num2 * number
			subList.append(multiply)#Adds the section of mltiplication
			
		list.append(subList)
	output += '\n   -----------------\n'
	
	for item in list:
		for subitem in item:#Outputs item neatly
			output += ' {} '.format(subitem)
		output += '\n'
	return output
#########################MAIN PROGRAM#########################


start = int(raw_input("Choose a starting number: "))
end = int(raw_input("Choose an ending number: "))
print (multi_table(start, end))