def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    vocab_words_1 = [vocab_words[0]]
    for word in vocab_words[1:]:
        vocab_words_1.append(vocab_words[0] + word)
    return " :: ".join(vocab_words_1)

def remove_suffix_ness(word):
        return word[:-5] + "y" if word.endswith("iness") else word[:-4]

def adjective_to_verb(sentence, index):
    word = sentence.split()[index]
    return word.strip(".,!?") + "en"