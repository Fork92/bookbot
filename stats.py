def get_word_list(book_text):
    return book_text.split()


def get_num_words(book_text):
    splitted_text = get_word_list(book_text)
    return len(splitted_text)


def count_character(text):
    lowercase_text = text.lower()
    caracter_dic = {}

    for c in lowercase_text:
        if c in caracter_dic:
            caracter_dic[c] = caracter_dic[c] + 1
        else:
            caracter_dic[c] = 1

    return caracter_dic


def sort_dict(character_dic):
    char_list = []
    for c in character_dic:
        char_dic = {"char": c, "num": character_dic[c]}
        char_list.append(char_dic)

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(items):
    return items["num"]
