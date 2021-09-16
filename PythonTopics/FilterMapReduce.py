from functools import reduce

nums = [2, 3, 5, 1, 7, 9, 8, 6, 4, 0]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

conVal = list(map(lambda n: n + 2, nums))
print(conVal)

sum = reduce(lambda a, b: a + b, nums)
print(sum)

square = lambda x: x * x
cube = lambda x: x * x * x

calList = [square, cube]

for i in range(1, 6):
    val = list(map(lambda x: x(i), calList))
    print(val)
