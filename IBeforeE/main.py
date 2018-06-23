def check(word):
  temp = ""
  for letter in word:
    if temp == "ei" and letter != "c": return False    
    if temp == "ie" and letter == "c": return False
    temp += letter
    if len(temp) > 2: temp = temp[1:]
  
  return True

word = input("Enter word to proceed or q to quit:\n")

while word != "q":
  print(check(word))
  word = input("Enter word to proceed or q to quit:\n") 