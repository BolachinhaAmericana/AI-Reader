
def file_reader_to_list(path_to_file: str):
    '''Reads File to List Format'''
    with open(path_to_file, 'r', encoding= 'utf8') as file_content_list:
        content_list = [content_list.rstrip() for content_list in file_content_list]
    content_list= list(set(content_list))
    if "" in content_list:
        content_list.remove("")
    return content_list

def get_words_and_abrevisions(data):
    '''Gets all Words in Lines / Individually / Abreviations'''
    all_words = [line.split(' ') for line in data]

    for lines in all_words:
        if ',' in lines[-2]:
            lines[-2] = lines[-2][:-1]

    singular_words = [word for singles in all_words for word in singles]
    all_abreviations = [words[-1] for words in all_words]

    return singular_words, all_words, all_abreviations

def get_dir_name_1():
    letters = 'abcdefghijklmaopqr'
    dir_names_1 = [f"{letter}0{x+1}" for letter in letters for x in range(6)]
    dir_names_1 = dir_names_1[:-4]
    return dir_names_1
