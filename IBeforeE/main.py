def check(word):
  temp = ""
  i = -1
  while i * -1 <= len(word):
    print(word[i])
    i -= 1
  # for letter in word:
  #   if temp == "ei" and letter != "c": return False    
  #   if temp == "ie" and letter == "c": return False
  #   temp += letter
  #   if len(temp) > 2: temp = temp[1:]
  
  return True

word = input("Enter word to proceed or q to quit:\n")

while word != "q":
  print(check(word))
  word = input("Enter word to proceed or q to quit:\n") 