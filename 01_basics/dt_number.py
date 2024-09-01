import math
import random
from decimal import Decimal
from fractions import Fraction

x = 5
y = 6
z = 3.0
f_name= 'SA'
l_name= 'Rajpoot'
print("x = 5\ny = 6\nz = 3.0\nf_name= 'SA'\nl_name= 'Rajpoot'\n")

print("x + y:" , x + y)
print("x + z:" , x + z)
print("x, y, z:" , x,y,z)
print("f_name + l_name:",f_name + l_name)

list1 = [1,5,3]
list2 = list1
print("list1",list1 ,"\nlist2", list2)
list1[0] = 44
print("after list1[0]=44")
print("list1",list1 ,"\nlist2", list2)

print('Comparision Operatops \n >, <, >=, <=, ==, !=, True/False')
print('Chained Comparision \n x < y < z \n x < y and y < z')

print('import math\t// to use math functions')
print('\nmath.floor(3.5)', math.floor(3.5))
print('math.floor(-3.5)', math.floor(-3.5))
print('math.floor(3.6)', math.floor(3.6))
print('math.floor(3.9)', math.floor(3.9))
print('\nmath.trunc(2.8)', math.trunc(2.8))
print('math.trunc(-2.8)',math.trunc(-2.8))

print('\nNumber System')
print('Ocatal: 0o20',0o20)
print('Hexal: 0xFF',0xFF)
print('Binary: 0b1000',0b1000)
print('oct(64):',oct(64))
print('bin(16):',bin(16))
print('hex(64):',hex(64))


print("\n\nimport random")
print("random.random():", random.random())
print("random.randint(1,100):", random.randint(1,100))

l1 = ['lemon','masala','ginger','mint']
print("l1 = ",l1)
print("random.choice(l1):", random.choice(l1))
random.shuffle(l1)
print("after random.shuffle(l1):", l1)
print("random.shuffle(l1):", random.shuffle(l1))

print("\import math\nimport random\nfrom decimal import Decimal\nfrom fractions import Fraction")


