"""
섭씨온도를 입력받아 화씨온도로 변환하세요
"""

def fahrenheit(celsius):
    return ((9/5)* float(celsius))+32


print("변환하고 싶은 섭씨 온도를 입력하세요")
user_input = input()

print(type(user_input), user_input)

fah = fahrenheit(user_input)
print('섭씨 온도: '+ user_input)
print(f'섭씨 온도: {user_input}')
print('화씨 온도: {0:.2f}'.format(fah))
print(f'화씨 온도: {round(fah,2)}')
