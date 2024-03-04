# 문제 1. 음수만 더해주세요
# 새로운 리스트에 음수만 더해서 리스트를 출력해주세요
"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
"""
"""
ex1_list = [3223, 42, -3, 85, -238, 68, 12]
ex2 = []
for i in range(len(ex1_list)):
    if
print(ex1_list([)i))


"""
"""
문제 2
새로운 리스트에 kia, hyundai를 추가하라.
"""
"""
ex2 = []

cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']

for i in range(len(cars)):
    if cars[i] == 'kia' or cars[i] == 'hyundai':
        ex2.append(cars[i])
print(ex2)
"""

"""
문제 3
25 ~ -15까지 -2 감소하는 결과를 리스트로 출력해줘유
range
"""
"""
ex1 = []
for i in range(25, -25, -2):
    ex1.append(i)

print(ex1)
"""



"""
문제 4 Range advanced
1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력
"""
"""
ex1 = []
for i in range(1, 16, +1):
    if i%2 == 0:
        ex1.append(i*10)
    else :
        ex1.append(i)
print(ex1)

ex2 = [i*10 if i % 2 == 0 else i for i in range(1,16)]

print(f'ex2 >>>> {ex2}')
"""

"""
# value 다 더해주세요(sum)

d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}
a = 0
for i in d.values():
    a += i
print(a)

b = sum(d.values())
print(b)
"""

"""
d = {'a': 'apple', 'b': 'banana'}
d = {'a': 'apple', 'b': 'banana', 'c': 'kiwi', 'd' : 'grape'}
업데이트 해주세요~
"""
"""
d = {'a': 'apple', 'b': 'banana'}
d = {'a': 'apple', 'b': 'banana', 'c': 'kiwi', 'd' : 'grape'}

f.
"""
"""
d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}

value가 150 이상인 값만 더해주세유

"""
"""
d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}
a=0
for i in d.values():
    if i > 150:
        a+=i
print(a)
"""
