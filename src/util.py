import random
word_list = []
possible_words = []
def load_word_list():
    with open('word_list.txt', 'r') as f:    
        global word_list
        word_list = f.read().split('\n')
        word_list = word_list[:-1]

def find_word(syllable):
    global possible_words
    possible_words = []    
    for word in word_list:
        if word.count(syllable) >= 1:
            possible_words.append(word)

def get_word():
    global possible_words
    return random.sample(possible_words, min(5, len(possible_words)))

if __name__ == '__main__':
    load_word_list()

    # print(word_list)
    syl = input('enter syllable to query: ')
    find_word(syl)
    print(get_word())
