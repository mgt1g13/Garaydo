import sys

if(len(sys.argv) < 2):
	print("Please, provide the file name!")
	exit()


print("Lexing file -> " + sys.argv[1]);


reserved_words = ["int","float", "char", "do", "for", "while", "if", "else"]
delimiters = ["(", ")", "{", "}", ";"]
arithmetic_ops = ["+", "-", "*", "/", "=", "%"]
logic_ops = ["<", "<=", ">", ">=", "!=", "=="]



f = open(sys.argv[1])


def next_char():
	global f
	return f.read(1)

def get_number():
	#Lê um número composto por digitos
	current_number = ""
	global current_char
	while(current_char.isdigit()):
		current_number += current_char
		current_char = next_char()
	return current_number

def get_word():
	#Lê uma palavra até encontrar um caractere não alfabético
	current_word = ""
	global current_char
	while(current_char.isalpha() or current_char.isdigit()):
		current_word += current_char
		current_char = next_char()
	return current_word


def get_comment():
	#Le um comentario até encontrar o fechamento do mesmo
	comment = ""
	global current_char
	current_char = next_char()
	while True:
		if (current_char == "*"):
			comment += current_char
			current_char = next_char()
			if(current_char == "/"):
				comment += current_char
				break
			else:
				continue
		comment += current_char
		current_char = next_char()

	return comment









current_char = next_char()


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
			print("[FLOAT," + current_number + "]")
		else:
			print("[INT," + current_number + "]")

	#Palavras e identificadores
	elif(current_char.isalpha()):
		current_word = get_word()
		if (current_word in reserved_words):
			print("[RESERVED_WORD, " + current_word + "]")

		else:
			print("[ID, " + current_word + "]")

	#Comentarios
	elif(current_char == "/"):
		current_char = next_char()
		if(current_char == "*"):	#caso seja um comentario
			comment = "/" + current_char + get_comment()
			print("[COMMENT, " + comment + "]")
			current_char = next_char()

		else:	#caso fosse apenas uma /
			print("[ARITHMETIC_OP, /]")
			continue


	#Operadores aritmeticos
	elif(current_char in arithmetic_ops):
		if(current_char == "/"):
			current_char = next_char()
			if(current_char == "/" or current_char == "*"):
				continue
		print("[ARITHMETIC_OP, " + current_char + "]")
		current_char = next_char()
		continue


	#Operadores logicos
	elif(current_char in logic_ops):
		print("[LOGIC_OP, " + current_char + "]")
		current_char = next_char()
		continue

	#Delimitadores
	elif(current_char in delimiters):
		print("DELIMITER, " + current_char + "]")
		current_char = next_char()
		continue


	else:
		print("Lexical Error!!!")
		exit()
