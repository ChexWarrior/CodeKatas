
file_name = input("Enter file name:\n")

try:
  input_file = open(file_name, 'r')
except OSError:
  print("File does not exist, exiting...\n")


