"""
мой вариант решения заданий из книги "Карьера программиста" Г.Л. Макдауэлл
"""

"""
Все ли символы в строке встречаются один раз Q1.1 (без ограничений)
"""
def ind_find(set_line, symb):
    for i,s in enumerate(set_line):
        if s == symb:
            return i
def once_symb(line):
    flag = None
    set_line = list(set(line))# все символы по одному разу
    bool_line = [-1] * len(set_line)
    for symb in line:
        if bool_line[ind_find(set_line, symb)] == -1:
            bool_line[ind_find(set_line, symb)] = 1
        else:
            bool_line[ind_find(set_line, symb)] = 0
    if sum(bool_line) == len(bool_line): # все 1
        flag = 1
    else:
        flag = 0
    return flag
#%% тест задания
print(once_symb("Mamanak"))
print(once_symb("Martnds"))

"""
Все ли символы в строке встречаются один раз если разрешено использовать только строки Q1.1 (с ограничением)
"""
def once_symb_str(line):
    uniq_line = ""
    flag = "True"
    for symb in line:
        if not symb in uniq_line:
            uniq_line += symb
        else:
            return "False"
    return flag

print(once_symb_str("Mamanak"))
print(once_symb_str("Martnds"))

"""
Является ли строка перестановкой другой Q1.2 (метод)
"""
class my_comparation():
	def __init__(self, value):
		self.value = ''.join(sorted(value))

	def comb_test(self, other):
		if len(self.value) != len(other.value):
			return False
		else:
			for i in range(len(self.value)):
				if self.value[i] != other.value[i]:
					return False
			return True
#%% тест задания
lin1 = my_comparation("dgvjkvgdg")
lin2 = my_comparation("vdgjkvgdg")
lin3 = my_comparation("ghv")
print(lin1.comb_test(lin3))
print(lin1.comb_test(lin2))

"""
Замена пробелов на %20 задание Q1.3 (метод inplace)
"""
class my_str_class():
	def __init__(self, value):
		self.value = value
		self.ind = 0
		self.flag = True

	def __symb_inplace(self):
		ind = self.ind
		self.value = self.value[:ind] +'%20' + self.value[ind+1:]
		return self
	
	def line_inplace(self):
		self.flag = True
		while self.flag:
			self.flag = True
			for i, s in enumerate(self.value):
				if s == " ":
					self.ind = i
					self.__symb_inplace()
					break
				if i == len(self.value) - 1:
					self.flag = False
					break
		return self
#%% тест задания
str_greet = 'Hello to you, young Padavan!'
g = my_str_class(str_greet)
g.line_inplace()
print(g.value)

"""
Проверка, является ли слово палиндромом задание Q1.4
"""
def palindrom(line):
	uniq = list(set(line))
	uniq.sort()
	S = []
	for s in uniq:
		S.append(line.count(s))
		even = list(filter(lambda n: n%2, S))
	if (len(even) == 1 and sum(S) % 2) or (len(even) == 0 and not sum(S) % 2):
		return True
	else:
		return False
line_test = "helleh"
line = "hello fllo"
print(palindrom(line))

"""
Находится ли слово на расстоянии одной модификации. Задание Q1.5
"""
#%% вставка символа
def insert_mod(line, mod_line):
	if len(line) + 1 != len(mod_line):
		return False
	counter = 0
	for i in range(len(line)):
		if line[i] != mod_line[i+counter]:
			counter +=1
			if counter > 1:
				return False
	return True

#%% удаление символа
def remove_mod(line, mod_line):
	return insert_mod(mod_line, line)
#%% замена символа
def change_mod(line, mod_line):
	counter = 0
	if len(line) != len(mod_line):
		return False
	for s, s_m in zip(line, mod_line):
		if s != s_m:
			counter += 1
	if counter < 2:
		return True
	else:
		return False
# проверка одна модификация или нет модификации
def one_mod(line, mod_line):
	if line == mod_line:
		return True
	else:
		return insert_mod(line, mod_line) | remove_mod(line, mod_line) | change_mod(line, mod_line)
#%% Тест
line_test = "heleh"
line_test1 = "helelh"
line_test2 = "helegh"
line_test3 = "gnae"
print(one_mod(line_test1, line_test3))
