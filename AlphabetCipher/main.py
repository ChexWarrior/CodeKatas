message = input('Please enter the message to encrypt...\n')
secret_word = input('Please enter the secret word...\n')
encrypted_msg = ""

print('You entered {0} for the message and {1} for the secret word!'.format(message, secret_word))

values = (
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

secret_word_pad = secret_word

# TODO Handle case when secret_word is longer than message
while len(secret_word_pad) < len(message):
  secret_word_pad += secret_word

if len(secret_word_pad) > len(message):
  diff = len(secret_word_pad) - len(message)
  slice_point = len(secret_word_pad) - diff
  #print('Slice point is {0}'.format(slice_point))
  secret_word_pad = secret_word_pad[:slice_point]

print(message)
print(secret_word_pad)

i = 0
for letter in message:
  # print(letter)
  # print(secret_word_pad[i])
  col_offset = values.index(secret_word_pad[i])
  row_offset = values.index(letter)
  key = col_offset + row_offset
  overflow = key - len(values)

  if overflow > 0:
    key = overflow
  
  encrypted_msg += values[key]
  i += 1

print('Encrypted message is: {0}'.format(encrypted_msg))


