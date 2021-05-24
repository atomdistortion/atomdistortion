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

