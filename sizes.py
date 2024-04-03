import sys

names = ('Tato') * 100

print(len(names))
print(sys.getsizeof(names))
print(sys.getsizeof('Tato'))
