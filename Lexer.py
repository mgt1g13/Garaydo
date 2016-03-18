import sys

if(len(sys.argv) < 2):
	print("Please, provide the file name!")
	exit()


print("Lexing file -> " + sys.argv[1]);


reserved_words = ["int","float", "char", "do", "for", "while", "if", "else"]
delimiters = ["(", ")"]
arithmetic_ops = ["+", "-", "*", "/"]



f = open(sys.argv[1])


def next_char():
	global f
	return f.read(1)


current_char = next_char()
# c = " "
# while(c):
# 	c = next_char()
# 	if(c):
# 		print(c)



def get_number():
	current_number = ""
	global current_char
	while(current_char.isdigit()):
		current_number += current_char
		current_char = next_char()
	return current_number


while(current_char):

	if(current_char == " " or current_char == "\n"):
		current_char = next_char()
		continue
	#Floats e Inteiros
	elif(current_char.isdigit()):
		current_number = get_number()
		if(current_char == "."):
			current_char = next_char()
			current_number += "." + get_number()
			print("[FLOAT," + current_number+ "]")
		else:
			print("[INT," + current_number+ "]")

		

	else:
		print("Lexical Error!!!")
		exit()





