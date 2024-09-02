fruit  = "Banana"
color = input("Enter the color of fruit (Brown, Yellow, Green): ")
# Green = Unripe,   Yellow = Ripe   Brown = Overripe

if fruit == "Banana":
  if color == "Green":
    print("Unripe")
  elif color == "Yellow":
    print("Ripe")
  elif color == "Brown":
    print("OverRipe")
  else:
    print("Enter the color of fruit (Brown, Yellow, Green)")