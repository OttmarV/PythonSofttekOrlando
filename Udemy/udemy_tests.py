import random

print(random.randint(1,6))


x = range(1,5)
print(type(x))
print(list(enumerate(list(x))))

for i, v in enumerate(x):
    print(i,v)


x = list(range(1,10))
print(x)
print("".split())
print(list("egggs"))

print("gg" in "eggs")