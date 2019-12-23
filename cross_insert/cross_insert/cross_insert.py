"""
返回一个列表，第二个列表交叉插入第一个列表
"""


def crossInsert(L1, L2):
	if not isinstance(L1, list):
		raise ValueError('{} is not a list'.format(str(L1)))
	if not isinstance(L2, (list, tuple)):
		raise ValueError('{} is not list or tuple'.format(str(L2)))
	import copy

	last_list = copy.copy(L1)

	len_of_list = len(last_list)
	len_of_date = len(L2)

	if not len_of_list == len_of_date:
		raise ValueError('two parameters length is not equal')

	times = range(1, (len_of_list * 2) - 1, 2)

	for i in range(len_of_list):
		try:
			pos = times[i]
			last_list.insert(pos, L2[i])
		except IndexError as e:
			last_list.append(L2[i])

	return last_list


if __name__ == '__main__':
	movies = ['The Holy Grail', 'The Life of Brian', 'The Meaning of Life']
	L2 = [1975, 1979, 1983]
	print(crossInsert(movies, L2))
