chai = "chai masala chai"
first_char = chai[0]
last_char = chai[-1]
print("first_char = chai[0]: ", first_char)
print("last_char = chai[0]: ", last_char)

num_list = "0123456789"
print("\nnum_list\t:",num_list)
print("num_list[:]\t:",num_list[:])
print("num_list[3:]\t:",num_list[3:])
print("num_list[:7]\t:",num_list[:7])
print("num_list[0:7:2]\t:",num_list[0:7:2])
print("num_list[0:7:3]\t:",num_list[0:7:3])
print("\nchai.upper()\t:",chai.upper())
print("chai.lower()\t:",chai.lower())
print("chai.strip()\t:",chai.strip())
print("chai.find('chai')\t:",chai.find('chai'))
print("chai.count('chai')\t:",chai.count('chai'))
print("chai.replace('masala','lemon')\t:",chai.replace('masala','lemon'))
print("\nTo convert string to list")
chai = "Lemon, Mint, Masala, Ginger"
print("chai.split():",chai.split())
print("chai.split(', '):",chai.split(', '))
print("\nTo convert list to string")
print("''.join(chai):",''.join(chai))

chai_type = "Masala"
quantity = 2
print("\nchai_type=",chai_type)
print("quantity=",quantity)
order = "I ordered {} cups of {} of chai."
print("order = I ordered {} cups of {} of chai.")
print("order.format(quantity, chai_type) = ",order.format(quantity, chai_type))

chai = "Masala Chai"
print('len(chai)\t:',len(chai))
for letter in chai:
  print(letter)

chai = "He said, \"Masala chai is Awesome.\""
print(chai)
chai = "Masala\nChai"
print(chai)
chai = r"Masala\nChai"
print(chai)
address = r"c:\user\pwd"
print(address)
