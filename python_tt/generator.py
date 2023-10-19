import sys

def season_generator(*args):
    for arg in args:
        yield arg
        
g = season_generator('spring', 'summer', 'autumn', 'winter')
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

def func():
    print("first work") 
    yield 1
    
    print("second work")
    yield 2
    
    print("third work")
    yield 3
    
ge = func()
# data = ge.__next__()
# # print(data)
# data = ge.__next__()
# # print(data)
# data = ge.__next__()
# # print(data)

double_generator = (i * 2 for i in range(1, 10))

list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = (i * 3 for i in range(1, 10000 + 1))

print("[list] sys.getsizeof :", sys.getsizeof(list_data))
print("[generator] sys.getsizeof :", sys.getsizeof(generator_data))