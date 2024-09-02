tea_types = ("Black","Green","Oolong")
print('tea_types = ', tea_types)
print('len(tea_types) = ', len(tea_types))
tea_more = ("Herbal", "Earl Grey")
tea_all = tea_types + tea_more
print('tea_types = ', tea_types)
print('tea_more = ', tea_more)
print('tea_all= ', tea_all)

if "Green" in tea_more:
  print("I have green tea in more tea")

if "Green" in tea_types:
  print("I have green tea in tea types")

print("tea_all.count('Green') = ",tea_all.count("Green"))