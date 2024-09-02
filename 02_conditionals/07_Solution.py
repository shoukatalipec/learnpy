order_size = "Medium"
# size = small, medium, large
extra_shot = True

if extra_shot:
  coffee = order_size + " coffee with extra shot."
else:
  coffee = order_size + "coffee."

print(coffee)