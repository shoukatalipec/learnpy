print("Dictionary")

chai_types = {"Malasa":"Spicy","Ginger":"Zesty","Green":"Mild"}
print("chai_types=",chai_types) 
print("chai_types.get('Masala')=",chai_types.get('Masala')) 
print("chai_types.get('Gingery')=",chai_types.get('Gingery'))
chai_types["Green"] = "Fresh"
print("chai_types=['Green']='Fresh'",chai_types) 

for chai in chai_types:
  print(chai)

print("\nUsing key, value")
for chai in chai_types:
  print(chai, ": ",chai_types[chai])

print("\nUsing key, value syntax")
for key, values in chai_types.items():
  print(key, ": ",values)

if 'Malasa' in chai_types:
  print("I have masala")

print(len(chai_types))

chai_types["Earl Grey"] = 'Citrus'
print("chai_types=",chai_types) 
print(len(chai_types))

chai_types.pop('Ginger')
print("chai_types=",chai_types) 
print(len(chai_types))

chai_types.popitem()
print("chai_types=",chai_types) 
print(len(chai_types))

del chai_types["Green"]
print("chai_types=",chai_types) 
print(len(chai_types))

chai_types_c = chai_types
print("chai_types=",chai_types) 
print("chai_types_c=",chai_types_c) 

print("\nDictionary with a Dictionary")

tea_shop = {
  "Chai":{"Masala":"Spicy","Ginger":"Zest","Green":"Mild"},
  "Tea":{"Black":"Strong","Earl Grey":"Citrus"}
}

print("tea_shop = ",tea_shop)
print("tea_shop['Chai'] = ",tea_shop['Chai'])
print("tea_shop['Chai']['Ginger'] = ",tea_shop['Chai']['Ginger'])

square_number = {x:x**2 for x in range(6)}
print("square_number = ",square_number)
square_number.clear()

keys = ['Masala,','Ginger','Lemon']
default_value = "Delicious"
new_dic = dict.fromkeys(keys, default_value)
print("new_dict:", new_dic)

print("Video at 4:41 end")