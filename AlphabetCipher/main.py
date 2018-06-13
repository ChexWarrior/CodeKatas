message = input('Please enter the message to encrypt...')
secret_word = input('Please enter the secret word...')

print('You entered {0} for the message and {1} for the secret word!'.format(message, secret_word))

values = (
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

# extend secret_word out to same length as message
secret_message = ""

while len(secret_message) < len(message):
  secret_message += secret_word

if len(secret_message) > len(message):
  diff = len(secret_message) - len(message)
  slice_point = len(secret_message) - diff
  #print('Slice point is {0}'.format(slice_point))
  secret_message = secret_message[:slice_point]

print(message)
print(secret_message)

