file_name = input("Enter file name:\n")

try:
  input_file = open(file_name, 'r')
except OSError:
  print("File does not exist, exiting...\n")

input_line1 = input_file.readline().split(" ")
input_line2 = input_file.readline().split(" ")

coins = []
total = 0

for i in range(1, len(input_line1)):
  if i == 1: 
    total = input_line1[i]
  else:
    coins.append(input_line1[i])

