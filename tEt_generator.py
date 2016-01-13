from itertools import product


def tEt_generator(num):
	for project in [''.join(i) for i in product("10",repeat=num)]:
		print project


tEt_generator(8)