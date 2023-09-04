import nltk

# nltk.download("wordnet")
# python -m spacy download en_core_web_sm

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

import spacy

stemmer = PorterStemmer()

word1, word2 = "cars", "revolution"

print(stemmer.stem(word1), stemmer.stem(word2))

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better", pos="a"))

nlp = spacy.load("en_core_web_sm")
token = nlp("better")
for word in token:
    print(word.text, word.lemma_)

doc = nlp(
    "Charles Spencer Chaplin was born on 16 April 1889 toHannah Chaplin (born Hannah Harriet Pedlingham Hill) and Charles Chaplin Sr"
)
for token in doc:
    print(
        token.text,
        token.lemma_,
        token.pos_,
        token.shape_,
        token.is_alpha,
        token.is_stop,
    )
