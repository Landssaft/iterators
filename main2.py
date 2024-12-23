my_list_simple = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

my_list_hard = [
    [],
    [1, [2], 3, 4, [5, 6, 7]],
    [8, 9, 10, 11],
    [12, 13, 14, [[[[15]]]]], []
]

class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)

        return self.nested_list[self.nested_list_cursor]

from itertools import chain

class FlatIteratorEasyWay:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        return chain.from_iterable(self.multi_list)

def flat_generator(my_list):
     for sub_list in my_list:
         for item in sub_list:
             yield item

class FlatIteratorV2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)

            except StopIteration:
                if not self.iterators_queue:

                    raise StopIteration
                else:

                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):

                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:

                return self.current_element

def flat_generator_v2(multi_list):
    for item in multi_list:
        if isinstance(item, list):

            for sub_item in flat_generator_v2(item):
                yield sub_item
        else:
            yield item

print('Задача 1')
for item in FlatIterator(my_list_simple):
    print(item)
print('*' * 25)

print('Задача 2')
for item in flat_generator(my_list_simple):
     print(item)
print('*' * 25)

print('Задача 3')
for item in FlatIteratorV2(my_list_hard):
    print(item)
print('*' * 25)

print('Задача 4')
for item in flat_generator_v2(my_list_hard):
    print(item)
print('*' * 25)
print('Задача ниндзя итератор')
for item in FlatIteratorEasyWay(my_list_hard):
    print(item)
print('*' * 25)