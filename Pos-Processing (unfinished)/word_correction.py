import csv

from nltk.corpus import stopwords
from nltk.corpus import extended_omw
from Levenshtein import distance

tab = extended_omw.raw("/home/alepy/nltk_data/corpora/extended_omw/spa/wn-data-spa.tab")
count=0

words = [line.split('\t')[2] for line in tab.split('\n') if line]
omw_list=[] #Lista com as palavras do dataset omw e stopwords
for word in words:
    omw_list.append(word)

stp_words = stopwords.words('spanish')
for word in stp_words:
    omw_list.append(word)


def open_file(csv_path):
    prefered_words=[]

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                prefered_words.append(word)
    
    return prefered_words

csv_file = "/home/alepy/aia/text_gen/val/e/e.csv"
prefered_words = open_file(csv_file)

def find_most_accurate_word_csv(misspelled_word, csv_file_path):
    most_accurate_word = None
    min_distance = float('inf')


    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                current_distance = distance(misspelled_word, word)
                if current_distance < min_distance:
                    count=0
                    min_distance = current_distance
                    most_accurate_word = word
                if current_distance == min_distance:
                    count+=1
    
    if count > 2:
        "vai ao dictionary"
    
    
    return most_accurate_word

def find_most_accurate_word_dic(misspelled_word):
    most_accurate_word = None
    min_distance = float('inf')
    
    for word in omw_list:
        current_distance = distance(misspelled_word, word)
        if current_distance < min_distance:
            min_distance = current_distance
            most_accurate_word = word
    
    return most_accurate_word


def post(misspelled_word):

    if misspelled_word in prefered_words:
        pass



# Example usage:
misspelled = "Teuzolgía"
csv_file = "/home/alepy/aia/text_gen/val/e/e.csv"
accurate_word = find_most_accurate_word_csv(misspelled, csv_file)
print(f"The most accurate word is: {accurate_word}")

#accurate_word = find_most_accurate_word_dic(misspelled)
#print(f"The most accurate word is: {accurate_word}")


#print(prefered_words)

'''

se tiver no csv tabom
    se tiver uma aprox (palavras pequenas 3) 2 ou mais em relação ao csv e ele n tiver
    see n... se tiver no dicionario 
        se n tiver no dicionario fas aproximação para o dicionario

        

if csv: Done
else: 
    if csv.approx >=  (x): Done
    else:
    if Dict: Done
    else: Dict.approx 
    
'''