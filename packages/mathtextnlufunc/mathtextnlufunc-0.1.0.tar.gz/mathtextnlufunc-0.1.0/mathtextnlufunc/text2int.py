import re
from collections import Counter

# Change this according to what words should be corrected to
SPELL_CORRECT_MIN_CHAR_DIFF = 2

TOKENS2INT_ERROR_INT = 32202

ONES = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
]

CHAR_MAPPING = {
    "-": " ",
    "_": " ",
    "and": " ",
    ",": "",
}

TOKEN_MAPPING = {
    "and": " ",
    "oh": "0",
}


def words(text): return re.findall(r'\w+', text.lower())


NUMBERS = ['hundred', 'thousand', 'million', 'trillion', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
           'eighty', 'ninety', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
WORDS = Counter(NUMBERS)

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def find_char_diff(a, b):
    # Finds the character difference between two str objects by counting the occurences of every character. Not edit distance.
    char_counts_a = {}
    char_counts_b = {}
    for char in a:
        if char in char_counts_a.keys():
            char_counts_a[char] += 1
        else:
            char_counts_a[char] = 1
    for char in b:
        if char in char_counts_b.keys():
            char_counts_b[char] += 1
        else:
            char_counts_b[char] = 1
    char_diff = 0
    for i in char_counts_a:
        if i in char_counts_b.keys():
            char_diff += abs(char_counts_a[i] - char_counts_b[i])
        else:
            char_diff += char_counts_a[i]
    return char_diff


def tokenize(text):
    text = text.lower()
    # print(text)
    text = replace_tokens(''.join(i for i in replace_chars(text)).split())
    # print(text)
    text = [i for i in text if i != ' ']
    # print(text)
    output = []
    for word in text:
        # print(word)
        out_num = convert_word_to_int(word)
        if out_num == TOKENS2INT_ERROR_INT:
            return TOKENS2INT_ERROR_INT
        else:
            output.append(out_num)
    output = [i for i in output if i != ' ']
    # print(output)
    return output


def detokenize(tokens):
    return ' '.join(tokens)


def replace_tokens(tokens, token_mapping=TOKEN_MAPPING):
    return [token_mapping.get(tok, tok) for tok in tokens]


def replace_chars(text, char_mapping=CHAR_MAPPING):
    return [char_mapping.get(c, c) for c in text]


def convert_word_to_int(in_word, numwords=None):
    # Converts a single word/str into a single int
    teens = {
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    if not numwords:
        numwords = dict(teens)
        for idx, word in enumerate(ONES):
            numwords[word] = idx
        for idx, word in enumerate(tens):
            numwords[word] = idx * 10
        for idx, word in enumerate(scales):
            numwords[word] = 10 ** (idx * 3 or 2)
    if in_word in numwords:
        # print(in_word)
        # print(numwords[in_word])
        return numwords[in_word]
    try:
        int(in_word)
        return int(in_word)
    except ValueError:
        pass
    """
    # Spell correction using find_char_diff
    char_diffs = [find_char_diff(in_word, i) for i in ONES + tens + scales]
    min_char_diff = min(char_diffs)
    if min_char_diff <= SPELL_CORRECT_MIN_CHAR_DIFF:
        return char_diffs.index(min_char_diff)
    """
    corrected_word = correction(in_word)
    if corrected_word in numwords:
        return numwords[corrected_word]
    # print(f'{in_word}=>corrected=>{corrected_word} not in numwords')
    if in_word in numwords:
        return numwords[in_word]
    # print(f'{in_word} not in numwords')
    return TOKENS2INT_ERROR_INT


def tokens2int(tokens):
    # Takes a list of tokens and returns a int representation of them
    if tokens == TOKENS2INT_ERROR_INT:
        return TOKENS2INT_ERROR_INT
    types = []
    for i in tokens:
        if i <= 9:
            types.append(1)

        elif i <= 90:
            types.append(2)

        else:
            types.append(3)
    # print(tokens)
    if len(tokens) <= 3:
        current = 0
        for i, number in enumerate(tokens):
            if i != 0 and types[i] < types[i - 1] and current != tokens[i - 1] and types[i - 1] != 3:
                current += tokens[i] + tokens[i - 1]
            elif current <= tokens[i] and current != 0:
                current *= tokens[i]
            elif 3 not in types and 1 not in types:
                current = int(''.join(str(i) for i in tokens))
                break
            elif '111' in ''.join(str(i) for i in types) and 2 not in types and 3 not in types:
                current = int(''.join(str(i) for i in tokens))
                break
            else:
                current += number

    elif 3 not in types and 2 not in types:
        current = int(''.join(str(i) for i in tokens))

    else:
        """
        double_list = []
        current_double = []
        double_type_list = []
        for i in tokens:
            if len(current_double) < 2:
                current_double.append(i)
            else:
                double_list.append(current_double)
                current_double = []
        current_double = []
        for i in types:
            if len(current_double) < 2:
                current_double.append(i)
            else:
                double_type_list.append(current_double)
                current_double = []
        print(double_type_list)
        print(double_list)
        current = 0
        for i, type_double in enumerate(double_type_list):
            if len(type_double) == 1:
                current += double_list[i][0]
            elif type_double[0] == type_double[1]:
                current += int(str(double_list[i][0]) + str(double_list[i][1]))
            elif type_double[0] > type_double[1]:
                current += sum(double_list[i])
            elif type_double[0] < type_double[1]:
                current += double_list[i][0] * double_list[i][1]
        #print(current)
        """
        count = 0
        current = 0
        for i, token in enumerate(tokens):
            count += 1
            if count == 2:
                if types[i - 1] == types[i]:
                    current += int(str(token) + str(tokens[i - 1]))
                elif types[i - 1] > types[i]:
                    current += tokens[i - 1] + token
                else:
                    current += tokens[i - 1] * token
                count = 0
            elif i == len(tokens) - 1:
                current += token

    return current


def text2int(text):
    # Wraps all of the functions up into one
    return tokens2int(tokenize(text))
