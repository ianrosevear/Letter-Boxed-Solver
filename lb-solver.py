import sys


# returns a dictionary mapping letters to possible next letters
def possible_letters(sides):

    possible_next_letters = {}
    for curr_side in sides:
        other_side_letters = ' '.join([side for side in sides if side is not curr_side])
        for c in curr_side:
            possible_next_letters[c] = other_side_letters

    return possible_next_letters


# returns a trimmed wordlist with only valid words given valid next letters
def possible_words(wordlist, valid_letters):

    trimmed_wordlist = []
    
    for w in wordlist:

        word = w.lower().strip()
        w_length = len(word)
        if w_length < 3:
            continue

        first_letter = word[0]
        if first_letter not in valid_letters:
            continue

        valid_next = valid_letters.get(first_letter)
        for i in range(1, w_length):
            curr_letter = word[i]

            # letter isn't on any side
            if curr_letter not in valid_letters:
                break

            # letter isn't valid given previous letter
            if curr_letter not in valid_next:
                break
            
            if i == (w_length - 1):
                trimmed_wordlist.append(word)
            else:
                valid_next = valid_letters.get(curr_letter)

    return trimmed_wordlist


# find pairs with word1 that cover every letter
def find_pairs(wordlist, word1, letters):
    pairs = []
    words = [w for w in wordlist if word1[-1] == w[0]]
    
    for word2 in words:
        remaining = [c for c in letters if c not in word1 and c not in word2]
        if len(remaining) == 0:
            pairs.append((word1, word2))

    return pairs


def main(wordlist_file):

    with open(wordlist_file, 'r') as wordlist:
        
        wl = wordlist.readlines()
        sides = input('Enter the four sides separated by spaces: ').split()
        letters = ''.join(sides)
        valid_letters = possible_letters(sides)
        trimmed_wordlist = possible_words(wl, valid_letters)
        
        all_pairs = []
        for word in trimmed_wordlist:
            word_pairs = find_pairs(trimmed_wordlist, word, letters)
            for p in word_pairs:
                all_pairs.append(p)

        print(f"Found {len(all_pairs)} possible two word solutions:")
        for sol in all_pairs:
            print(f"{sol[0]} - {sol[1]}")


if __name__ == "__main__":
    main(sys.argv[1])