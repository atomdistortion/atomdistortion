"""
Casear and vigenere ciphir
"""
import sys
A = ord('A'); Z = ord('Z')
a = ord('a'); z = ord('z')
def e_let(ord_let, shift, k):
	return chr((ord_let - shift + k)%26 + shift)
def d_let(ord_let, shift, k):
	return chr((ord_let - shift - k)%26 + shift)

def csr_enc(line, k):
	ind = 0
	enc_line = ""
	for letter in line:
		ord_let = ord(letter)
		if (ord_let >= a and ord_let <= z):
			enc_line += e_let(ord_let, a, k[ind])
			ind += 1
		elif ord_let >= A and ord_let <= Z:
			enc_line += e_let(ord_let, A, k[ind])
			ind += 1
		else:
			enc_line += letter
		if ind == len(k):
			ind = 0
	return enc_line
	
def csr_dec(line, k):
	ind = 0
	dec_line = ""
	for letter in line:
		ord_let = ord(letter)
		if (ord_let >= a and ord_let <= z):
			dec_line += d_let(ord_let, a, k[ind])
			ind += 1
		elif ord_let >= A and ord_let <= Z:
			dec_line += d_let(ord_let, A, k[ind])
			ind += 1
		else:
			dec_line += letter
		if ind == len(k):
			ind = 0
	return dec_line
	
message = "\t Be sure to drink your Ovaltine!"

if len(sys.argv) == 2:
	user_msg = sys.argv[1]
elif sys.argv[0][-3:] == '.py':
	user_msg = input("Input a message: ")
else:
	user_msg = input("Input a message: ")
	
Ces_or_Ven = 'ven' # "ces" if you want to use cesar ciphir 
if Ces_or_Ven == 'ven':
	key_phrase = "Fear"
	k = []
	for i in key_phrase:
		k.append(ord(i))
elif Ces_or_Ven == 'ces':
	k = 13
enc_msg =csr_enc(user_msg, k)
dec_msg =csr_dec(enc_msg, k)
print('\t', enc_msg)
print('\t', dec_msg)
