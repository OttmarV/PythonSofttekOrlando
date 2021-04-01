"""
def func():
    i=1
    while i>0:
        yield i
        i-=1
print(type(func()))
for i in func():
    print(type(func()))
    print(type(i))
"""
"""
def func():
    i=1
    while i>0:
        return i
        i-=1
print(type(func()))
for i in func():
    print(i)
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_it = (n ** 2 for n in nums)
print(squares_it.__sizeof__())
squares_lst = [n ** 2 for n in nums]
print(squares_lst.__sizeof__())
squares_test = (n ** 3 for n in range(10000))
print(squares_test.__sizeof__())
