
# Remove all non alpha characters...
def scrub_pattern(pattern):
    scrubbed_pattern = ""
    
    for char in pattern:
        if char.isalpha():
            scrubbed_pattern += char

    return scrubbed_pattern    

def match_patterns(target_word, spaces, patterns):
    for pattern in patterns:
        print(scrub_pattern(pattern))
        # check if pattern even matches

        # if so then we nee

with open('./patterns.txt') as patterns:
    target_word = input('Enter word to hyphenate...')
    spaces = len(target_word) - 1
    match_patterns(target_word, spaces, patterns)