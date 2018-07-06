file_name = input("Enter file name:\n")

try:
  input_file = open(file_name, 'r')
except OSError:
  print("File does not exist, exiting...\n")

input_line1 = input_file.readline().split(" ")
input_line2 = input_file.readline().split(" ")

coins = []
total = 0
total_num_coins = int(input_line2[3])

# if false then we have a maximum amount of coins that can be used (n < 5)
# if true then we have a minimum number of coins to us (n > 5)
is_minimum = False

for i in range(1, len(input_line1)):
  if i == 1: 
    total = input_line1[i]
  else:
    coins.append(input_line1[i])

if input_line2[2] == "<":
  total_num_coins -= 1
elif input_line2[2] == ">":
  total_num_coins += 1
  is_minimum = True
elif input_line2[2] == ">=":
  is_minimum = True

if is_minimum: 
  print("Must use at least " + str(total_num_coins))
else:
  print("Must use at most " + str(total_num_coins))