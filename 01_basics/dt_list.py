tea_var = ['Black','Green','White','Oolong']

print("tea_var[1:3]\t:",tea_var[1:3])
print("tea_var[:2]\t:",tea_var[:2])
print("tea_var[1:]\t:",tea_var[1:])
print("tea_var[::2]\t:",tea_var[::2])
tea_var[3] = 'harbal'
print("\nAfter tea_var[3] = 'harbal'\ntea_var:",tea_var)
tea_var[1:2] = 'Lemon'
print("\nAfter tea_var[1:2] = 'Lemon'\ntea_var:",tea_var)

tea_var = ['Black','Green','White','Oolong']
print("tea_var[1:2]\t:",tea_var[1:2])
tea_var[1:2] = ['Lemon']
print("\nAfter tea_var[1:2] = ['Lemon']\ntea_var:",tea_var)
print("tea_var[1:3]\t:",tea_var[1:3])
tea_var[1:3] = ['Lemon','Masala']
print("\nAfter tea_var[1:3] = ['Lemon','Masala']\ntea_var:",tea_var)

print("tea_var[1:1]\t:",tea_var[1:1])
tea_var[2:2] = ['Test','Test']
print("tea_var\t:",tea_var)
tea_var[2:2] = []
print("tea_var\t:",tea_var)

for tea in tea_var:
 print(tea,end = "-")

if "Orange" in tea_var:
 print("I have Orange tea")

tea_var.append('Orange')
if "Orange" in tea_var:
 print("I have Orange tea")
print("tea_var\t:",tea_var)

tea_var.pop()
print("tea_var.pop()\t:",tea_var.pop())
print("tea_var\t:",tea_var)
tea_var.remove('Test')
print("tea_var\t:",tea_var)
tea_var.insert(3,'Blue')
print("tea_var\t:",tea_var)

print("\nwith tea_var_c = tea_var:",tea_var)
tea_var_c = tea_var
print("tea_var\t\t:",tea_var)
print("tea_var_c\t:",tea_var_c)

tea_var_c.append('Red Tea')
print("After Appending:")
print("tea_var\t\t:",tea_var)
print("tea_var_c\t:",tea_var_c)

print("\nwith tea_var_c = tea_var.copy():",tea_var)
tea_var_c = tea_var.copy()
print("tea_var\t\t:",tea_var)
print("tea_var_c\t:",tea_var_c)

tea_var_c.append('Red Tea')
print("After Appending:")
print("tea_var\t\t:",tea_var)
print("tea_var_c\t:",tea_var_c)
