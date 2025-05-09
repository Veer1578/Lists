L = [4, 5, 10, 7, 8, 1, 2]
print('Orignal list is ', L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print('Sum is ', count)
print('Average is ', avg)

L.sort()

print('Largest element ', L[-1])
print('Smallest element ', L[0])
