import sys

def get_num_words():
    with open(sys.argv[1]) as book:
        book_contents = book.read()

        num_words = 0
        list_book = book_contents.split()

        for word in list_book:
            num_words += 1

        return num_words

def count_all_lol():
    with open(sys.argv[1]) as franky:
        book = franky.read()
        list_book = book.split()
        char_list = []

        for word in list_book:
            for char in word:
                char_list.append(char.lower())

        dic_book = {}

        for char in char_list:
            if char.isalpha() == False:
                continue
            elif char in dic_book:
                dic_book[char] += 1
            else:
                dic_book[char] = 1

        return dic_book

def sorting():
    def sort_on(items):
        return items["num"]

    dic = count_all_lol()
    list_dict = []

    for key, value in dic.items():
        dict = {}
        dict["char"] = key
        dict["num"] = value
        list_dict.append(dict)
        
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict