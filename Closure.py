# Closure
# 함수가 종료되어도 자원을 사용할 수 있는 함수

# Closure 조건
## 내부 함수
## 외부 함수를 참조
## 외부 함수가 내부 함수를 반환

def outer(name):
    def inner():
        print(name, ", Hello!")
        
    return inner

func = outer("balang")
func()


def greeting(name, age, gender):
    def inner():
        print(f"{name}, Hello! | {age} | {gender}")
    return inner

closure = greeting("balang", 25, "male")
closure()
# print(dir(closure()))
# print(type(closure.__closure__))
# print(dir(closure.__closure__[0]))
# print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)