marks = 91

if marks > 100:
  print('Please verify your marks again.')
  exit()
elif marks > 90:
  grade = 'A'
elif marks > 80:
  grade = 'B'
elif marks > 70:
  grade = 'B'
elif marks > 60:
  grade = 'D'
elif marks > 50:
  grade = 'E'
else:
  grade = 'F'

print("Your grades are: ", grade)