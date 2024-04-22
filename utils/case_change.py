def snake_to_camel_case(word: str):
    splited = word.split("_")
    re_word = ""
    for index, item in enumerate(splited):
        if index > 0:
            re_word = re_word + item.capitalize()
        else:
            re_word = item

    return re_word
