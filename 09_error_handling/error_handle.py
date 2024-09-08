# file = open('youtube.txt','w')

# try:
#   file.write('This is youtube File')
# finally:
#   file.close()

with open('youtube.txt','w') as file:
  file.write('Youtube File2')