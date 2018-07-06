def check(word):
  temp = ""
  i = len(word) - 1
  while i > -1:
    current = word[i]
    if temp == "ei" and current != "c": return False    
    if temp == "ie" and current == "c": return False
    temp = current + temp

    if len(temp) > 2: 
      temp = temp[:len(temp) - 1]
      
    i -= 1
  
  return True

word = input("Enter word to proceed or q to quit:\n")

while word != "q":
  print(check(word))
  word = input("Enter word to proceed or q to quit:\n") 