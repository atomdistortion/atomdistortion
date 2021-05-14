"""
python fantasy on CS50 problem set (taken from /davidventuri/harvard-cs50)
set #1 mario tower
"""
def draw_line(i, n):
	spcs = n - i
	print(spcs*' ', end = '')
	print(i*'#')

def draw_fig(h, w):
	for i in range(h, 0, -1):
		draw_line(w-i, w)

def check_int(height):
		flag = 0
		try:
			height = int(height)
			flag = 1
		except:
			flag = 0
		return flag
		
def prompt_input():
		flag = 0
		height = -1000
		while not flag:
			height = input("input a nonneg num ls than 23: ")
			flag = check_int(height)
			if flag:
				height = int(height)
				if height < 0 or height >= 23:
					flag = 0
		return height
height = prompt_input()
flag = check_int(height)
draw_fig(height, 10)
