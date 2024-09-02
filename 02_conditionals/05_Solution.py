# Suggest an activity based on the weather (Sunny:Go for a walk, Rainy:Read a book, Snowy: Build a Snowman)

weather = (input("How is the weather today? (Sunny, Rainy, Snowy): ")).upper()

if weather == "SUNNY":
  print("Go for a walk.")
elif weather == "SNOWY":
  print("Build a snowman.")
elif weather == "RAINY":
  print("Read a book.")