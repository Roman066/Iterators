
#      Задание №1

class FlatIterator:
    def __init__(self, list_of_lists:list):
        self.list_of_lists = list_of_lists
        self.row = 0
        self.col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row >= len(self.list_of_lists) or self.col >= len(self.list_of_lists[self.row]):
            raise StopIteration
        else:
            val = self.list_of_lists[self.row][self.col]
            self.col += 1
            if self.col >= len(self.list_of_lists[self.row]):
                self.row += 1
                self.col = 0
            return val


list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

for x in FlatIterator(list_of_lists):
  	print(x)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item


    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()






#     Задание №2

import types


def flat_generator(list_of_lists:list):
    iter_object = iter(list_of_lists)
    while True:
        try:
            iter_object_values = next(iter_object)
            iter_object_enclosure = iter(iter_object_values)
            while True:
                try:
                    iter_object_enclosure_values = next(iter_object_enclosure)
                except StopIteration:
                    break
                yield iter_object_enclosure_values
        except StopIteration:
            break



list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
    ]

for x in flat_generator(list_of_lists_1):
    print(x)



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
        ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
