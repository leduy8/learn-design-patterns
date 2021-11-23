from collections.abc import Iterator, Iterable

class AlphabeticalOrderIterator(Iterator):
    def __init__(self, collection, reverse = False) -> None:
        self.collection = collection
        self.reverse = reverse
        self.position = -1 if self.reverse else 0

    def __next__(self):
        try:
            value = self.collection[self.position]
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection = []) -> None:
        self.collection = collection

    def __iter__(self):
        return AlphabeticalOrderIterator(self.collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self.collection, True)

    def add_item(self, item):
        self.collection.append(item)


collection = WordsCollection()
collection.add_item('First')
collection.add_item('Second')
collection.add_item('Third')
collection.add_item('Forth')

print("Straight traversal:")
print("\n".join(collection))

print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()))
    
