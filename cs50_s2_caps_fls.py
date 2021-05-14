prompt = input("please, enter your name: ")
def first_letters(prompt):
	arr = prompt.split(sep = ' ')
	up_cast = ""
	for i in arr:
		first_let = i[0]
		fl_ord = ord(first_let)
		if fl_ord >= ord('a') and fl_ord <= ord('z'):
			fl_ord -= ord('a') - ord('A')
		up_cast += chr(fl_ord)
	return up_cast

print('\t', first_letters(prompt))