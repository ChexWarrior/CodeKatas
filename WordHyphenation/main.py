
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

def get_scores(pattern):
    score_indices = {}

    for index, character in enumerate(pattern):
        if character.isdigit():
            score_indices[index] = character
    
    return score_indices

def score_match(spaces, word, pattern, scrubbed_pattern):
    # find index of match in target word
    match_index = word.find(scrubbed_pattern)
    
    # find index of scores in pattern
    scores = get_scores(pattern)

    # for each score add score index to match index
    num_scores = 0
    for index, value in scores.items():
        if index + match_index < len(spaces) and int(spaces[index + match_index]) < int(value):
            # each score already counted increases the count which needs to be accounted for
            spaces[index + match_index - num_scores] = value
            num_scores += 1

    return spaces

def hypenate(spaces, word):
    # remove first and last space since 
    # we can't hypenate those parts
    actual_spaces = spaces[1:-1]
    word_list = list(word)
    hypens_inserted = 1
    for index, value in enumerate(actual_spaces):
        if int(value) % 2 == 1:
            word_list.insert(index + hypens_inserted, '-')
            hypens_inserted += 1

    hypenated_word = ''.join(word_list)

    return hypenated_word

def process_patterns(target_word, spaces, patterns):
    for pattern in patterns:
        pattern = pattern.strip()
        scrubbed_pattern = scrub_pattern(pattern)
        checkStart = pattern[0] == '.'
        checkEnd = pattern[-1] == '.'
        is_match = check_match(target_word, scrubbed_pattern, checkStart, checkEnd)
        
        if is_match:
            print("Pattern: %s is a match!" % (pattern))
            spaces = score_match(spaces, target_word, pattern, scrubbed_pattern)
            
    print("Space Scores: %s" % (spaces))
    return hypenate(spaces, target_word)

with open('./patterns.txt') as patterns:
    target_word = input('Enter word to hyphenate: ')

    # count spaces before word start and after end
    spaces = [0] * (len(target_word) + 1)
    result = process_patterns(target_word, spaces, patterns)

    print("Result: %s" % (result))