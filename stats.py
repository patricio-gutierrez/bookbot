def get_num_words(text):
    splited_text = text.split()
    num_words = len(splited_text)
    return num_words


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def transform_dict(input_dict):
    result_list = []
    for key, value in input_dict.items():
        new_dict = {"word": key, "count": value}
        result_list.append(new_dict)
    return result_list

def sort_on(dict):
    return dict["count"]

def sort_words(input_dict):
    input_dict.sort(reverse=True, key=sort_on)
    return input_dict