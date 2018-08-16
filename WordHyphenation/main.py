
# Remove all non alpha characters...
def scrub_pattern(pattern):
    scrubbed_pattern = ""
    
    for char in pattern:
        if char.isalpha():
            scrubbed_pattern += char

    return scrubbed_pattern

def is_match(word, pattern, checkStart, checkEnd):
    if(checkStart):
        return word.find(pattern) == 0
    elif(checkEnd):
        # if the index returned from find + length of scrubbed
        # pattern is last index
        return word.find(pattern) + len(pattern) == len(word)
    else:
        return pattern in word

def match_patterns(target_word, spaces, patterns):
    for pattern in patterns:
        scrubbed_pattern = scrub_pattern(pattern)
        checkStart = pattern[0] == '.'
        checkEnd = pattern[-1] == '.'
        is_match(target_word, scrubbed_pattern, checkStart, checkEnd)

        # check if pattern even matches

        # if so then we nee

with open('./patterns.txt') as patterns:
    target_word = input('Enter word to hyphenate...')
    spaces = len(target_word) - 1
    match_patterns(target_word, spaces, patterns)