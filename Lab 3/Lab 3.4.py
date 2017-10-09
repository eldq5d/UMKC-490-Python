from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import re, collections

# Import and read file
corpus = file('sample.txt').read()

# Tokenization and Lemmatization
corpusSent = sent_tokenize(corpus)
corpusWords = [word_tokenize(t) for t in corpusSent]

lemmatizer = WordNetLemmatizer()
corpusLem = []
for i in corpusWords:
    for word in i:
         corpusLem.append(lemmatizer.lemmatize(word))

# POS to identify and remove verbs
i = 0
while i <= len(corpusLem)-1:
    if ((pos_tag(corpusLem)[i][1] == 'VB') or (pos_tag(corpusLem)[i][1] == 'VBD') or
            (pos_tag(corpusLem)[i][1] == 'VBG') or (pos_tag(corpusLem)[i][1] == 'VBN') or
            (pos_tag(corpusLem)[i][1] == 'VBZ')):
        del corpusLem[i]
    i+=1

# Frequency and identification of top 5 words
def tokens(text):
    return re.findall('[a-z]+', text.lower())
WORDS = tokens(corpus)
WORD_COUNTS = collections.Counter(WORDS)
common = WORD_COUNTS.most_common(5)

# Identify sentences including top 5 words and concatentate for final summary
summ = ''
for sent in corpusSent:
    for word in sent.split(" "):
        if (word == common[0][0] or word == common[1][0] or word == common[2][0] or
            word == common[3][0] or word == common[4][0]):
            summ = summ + sent + "\n"
            break
print(summ)
