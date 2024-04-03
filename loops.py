colors =["red","green","blue","orange"]
"for value in list:"
for color in colors:
    print(color)
for i in range(0,10,2) :
    print(i)

print('last')
for i in range (0,10,-1):
    print(i)

c = colors
c.append(5)
print(f"{c = }")
print(f"{colors = }")
colors.append(27)
print(f"{c = }")
print(f"{colors = }")



print(f"{'red' in colors = }")
print(f"{'pink' in colors = }")
print(f"{'Red' in colors = }")
print(f"{c == colors = }")

a= colors.copy()
print(f"{a == c = }")
print(f"{a is c = }")
print(f"{a is colors = }")
print(f"{c is colors}")

print(f"{id(color) = }")
print(f"{id(c) = }")
print(f"{id(a) = }")