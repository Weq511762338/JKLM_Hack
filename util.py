
word_list = []
def load_word_list():
    with open('word_list.txt', 'r') as f:    
        global word_list
        word_list = f.read().split('\n')
        word_list = word_list[:-1]

def get_word(syllable):
    possible_words = []
    for word in word_list:
        if word.count(syllable) >= 1:
            possible_words.append(word)
    return possible_words



if __name__ == '__main__':
    load_word_list()

    # print(word_list)
    syl = input('enter syllable to query: ')
    print(get_word(syl))
