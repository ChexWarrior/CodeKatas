
# Remove all non alpha characters...
def scrub_pattern(pattern):
    scrubbed_pattern = ""
    
    for char in pattern:
        if char.isalpha():
            scrubbed_pattern += char

    return scrubbed_pattern

def check_match(word, pattern, checkStart, checkEnd):
    if(checkStart):
        return word.find(pattern) == 0
    elif(checkEnd):
        # if the index returned from find + length of scrubbed
        # pattern is last index
        return word.find(pattern) > -1 and word.find(pattern) + len(pattern) == len(word)
    else:
        return pattern in word

def match_patterns(target_word, spaces, patterns):
    for pattern in patterns:
        pattern = pattern.strip()
        scrubbed_pattern = scrub_pattern(pattern)
        checkStart = pattern[0] == '.'
        checkEnd = pattern[-1] == '.'
        is_match = check_match(target_word, scrubbed_pattern, checkStart, checkEnd)

        if is_match:
            print("Pattern: %s is a match!" % (pattern))

with open('./patterns.txt') as patterns:
    target_word = input('Enter word to hyphenate...')
    spaces = len(target_word) - 1
    match_patterns(target_word, spaces, patterns)