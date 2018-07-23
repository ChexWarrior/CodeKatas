def recursive_iterate(mylist, current_index):
  if current_index < len(mylist):
    recursive_iterate(mylist, current_index + 1)
    print(mylist[current_index])


value = 130 
coins = [100, 20, 18, 12, 5, 5]

recursive_iterate(coins, 0)