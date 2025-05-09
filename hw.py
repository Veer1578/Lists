squares = []

max = int(input('Enter max: '))
min = int(input('Enter min: '))

for i in range(min, max + 1):
    j = i ** 2
    squares.append(j)
    
print(squares)

even = []
odd = []

for i in squares:
 if i % 2 == 0:
     even.append(i)
 else:
     odd.append(i)

print(even)
print(odd)