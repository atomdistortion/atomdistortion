"""
python fantasy on CS50 problem set (taken from /davidventuri/harvard-cs50)
set #1 simple greedy algorithm (not optimized, it is not required there)
"""
CENTS = [1, 5, 10, 25, 50]
DOLLARS = [1, 5, 10, 25, 50, 100, 500, 1000]		
def find_min_ind_ge(money, coin_set):
	ind = 0
	for i, val in enumerate(coin_set):
		if val <= money:
			ind = i
	if ind == len(coin_set):
		ind -= 1
	return ind

def make_change(money, coin_set):
	change =[]
	rest_money = money
	while rest_money > 0:
		max_coin_ind = find_min_ind_ge(rest_money, coin_set)
		rest_money -= coin_set[max_coin_ind]
		change.append(coin_set[max_coin_ind])
	return change
def input_float():
	flag = 0
	while not flag:
		val = input("input a float number: ")
		try:
			val = float(val)
			flag = 1
		except:
			print("retry: ")
			flag = 0
	return val

def split_float(val):
		cents = round((val - int(val))* 100)
		dolrs = int(val)
		if val - 0.01*cents - dolrs >0:# we round up due to accountance
			cents += 1
		return [dolrs, cents]

def stripped_list(change, symb):
	uniq_vals = list(set(change))
	uniq_vals.sort(reverse=True)
	output_str = ""
	for u_v in uniq_vals:
		count_val = 0
		for v in change:		
			if v == u_v:
				count_val += 1
		output_str += str(count_val) + 'X' + str(u_v) + symb + '; '
	return output_str[:-2]

val = input_float()
print('You want to change: ', val)
dolrs, cents = split_float(val)
dolrs = make_change(dolrs, DOLLARS)
cents = make_change(cents, CENTS)
print(stripped_list(dolrs, '$'))
print(stripped_list(cents, 'c'))
# print('\t', make_change(dolrs, DOLLARS), "$", " ", make_change(cents, CENTS))
