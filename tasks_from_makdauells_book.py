# мой вариант решения заданий из книги "Карьера программиста" Г.Л. Макдауэлл
# %% Все ли символы в строке встречаются один раз Q1.1 (без ограничений)
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

print(once_symb("Mamanak"))
print(once_symb("Martnds"))

#%% Все ли символы в строке встречаются один раз если разрешено использовать только строки
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


# %% Замена пробелов на %20 задание Q1.3 (метод inplace)
class my_str_class():
	def __init__(self, value):
		self.value = value
		self.ind = 0
		self.flag = True

	def symb_inplace(self):
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
					self.symb_inplace()
					break
				if i == len(self.value) - 1:
					self.flag = False
					break
		return self
#%%
str_greet = 'Hello to you, young Padavan!'
g = my_str_class(str_greet)
g.line_inplace()
print(g.value)
