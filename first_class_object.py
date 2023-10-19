# 1. be available like data
# 2. Can be handed over to parameters
# 3. Can be used as a return value

def func(x, y):
    return x+y

add = func
print("add", add(3, 4))

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

calculator = [mul, div]
print("mul", calculator[0](5, 6))
print("div", calculator[1](10, 2))


def inputData():
    data = input("데이터 입력 >>>")
    return data

def start(func):
    print("입력한 데이터는", func())
    
start(inputData)


def plusTen(a):
    return a + 10

def func(x):
    return plusTen(x)

print("plusTen", func(5))