def check(word):
  temp = ""
  i = -1
  while i * -1 <= len(word):
    #print(word[i])
    current = word[i]
    # if temp == "ei" and current != "c": return False    
    # if temp == "ie" and current == "c": return False
    temp = current + temp
    # if len(temp) > 2: temp = temp[1:]
    print(temp)
    i -= 1
  
  return True

word = input("Enter word to proceed or q to quit:\n")

while word != "q":
  print(check(word))
  word = input("Enter word to proceed or q to quit:\n") 