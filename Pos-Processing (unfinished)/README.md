# AI Reader - Post_processing

## Folders Description

- `./extended_omw/` :\
Dir containing the spanish dataset from nltk.

### Requirements

- Step 1:
```
pip install nltk
```
- Step 2:
```
import nltk

# Download stopwords corpus
nltk.download('stopwords')

# Download extended OMW
nltk.download('omw')
```
- Step 3:
```
pip install python-Levenshtein
```

## Note
For some reason when we download the extended_omw the folder created in the `./nltk_data/corpora` directory is called omw and not extended_omw.
When we try to call him in the code it doesn't actually work because of this troubleshoot with the dirs.
To fix that we moved the spanish dataset (spa) and the other files (citation, LICENSE and README) to the `./extended_omw/` dir and then moved him to the 
`./nltk_data/corpora` so that would be fine calling this dataset on the code.

## Code

- To call the extended_omw dataset we needed to create a variable which is `tab`.
- First to `for` loops are to put together both datasets, extended_omw and stopwords.
  
### Functions
- `open_file`: Opens a csv file and append each word from each line on the `prefered_words` list.
- `find_most_accurate_word_csv`: Finds the most accurate word on the csv file (distance is the value that indicates how many characters are "wrong" comparing to the `misspelled_word` variable.
- `find_most_accurate_word_dic`: Does the same thing but this time in the `omw_list` (dictionary).

## How to run

- Don't forget to change the paths variables to open the csv file you want.
- The variable `misspelled` (in the end) is the word we will be comparing to the ones in the datasets.

After those changes just run:

```
python3 word_correction.py
```

