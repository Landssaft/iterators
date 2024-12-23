
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]

class FlatIterator:

	def __init__(self, my_list):
		self.my_list = my_list
		self.position = -1

	def __iter__(self):
		return self

	def __next__(self):
		new_list = sum(self.my_list, [])
		if len(new_list) - 1 == self.position:
			raise StopIteration
		else:
			self.position += 1
			return new_list[self.position]


def flat_generator(my_list):
	for i in my_list:
		for j in i:
			yield j


def flat_generator_rec(my_list):
	for i in my_list:
		if isinstance(i, list):
			yield from flat_generator(i)
		else:
			yield i


if __name__ == '__main__':
	for item in FlatIterator(nested_list):
		print(item)
	print('\n')

	for item in flat_generator(nested_list):
		print(item)
	print('\n')

	for item in flat_generator_rec(nested_list):
		print(item)