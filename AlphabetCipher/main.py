message = input('Please enter the message to encrypt...')
secret_word = input('Please enter the secret word...')

print('You entered {0} for the message and {1} for the secret word!'.format(message, secret_word))

values = (
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

# extend secret_word out to same length as message
extended_secret_word = ""

while len(extended_secret_word) < len(message):
  extended_secret_word += secret_word

if len(extended_secret_word) > len(message):
  diff = len(extended_secret_word) - len(message)
  slice_point = len(extended_secret_word) - diff
  #print('Slice point is {0}'.format(slice_point))
  extended_secret_word = extended_secret_word[:slice_point]

print(message)
print(extended_secret_word)

