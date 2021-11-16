def add(n1, n2):
    ##pass
    return n1 + n2

print(add(100,200))

# ctrl + shift + f10  --> 실행

add2 = lambda n1, n2: n1 + n2
print(add2(10,20))

print(type(add))
print(type(add2))

class User:
    # 생성자 선언
    def __init__(self, name):
        self.name = name
    # toString()
    def __str__(self):
        return self.name

#객체 생성
user1 = User("파이썬")
print(user1)

""" 
파이썬 모듈 안에는 함수와 클래스 등을 선언할 수 있다
"""

