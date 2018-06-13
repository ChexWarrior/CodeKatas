message = input('Please enter the message to encrypt...')
secret_word = input('Please enter the secret word...')

print('You entered {0} for the message and {1} for the secret word!'.format(message, secret_word))

values = (
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

# TODO Handle case when secret_word is longer than message
while len(secret_word) < len(message):
  secret_word += secret_word

if len(secret_word) > len(message):
  diff = len(secret_word) - len(message)
  slice_point = len(secret_word) - diff
  #print('Slice point is {0}'.format(slice_point))
  secret_word = secret_word[:slice_point]

print(message)
print(secret_word)

