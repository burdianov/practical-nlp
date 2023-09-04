import nltk

# nltk.download("stopwords")

from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "In the previous chapter, we saw examples of some common NLP applications that we might encounter in everyday life. If we were asked to build such an application, think about how we would approach doing so at our organization. We would normally walk through the requirements and break the problem down into several sub-problems, then try to develop a step-by-step procedure to solve them. Since language processing is involved, we would also list all the forms of text processing needed at each step. This step-by-step processing of text is known as pipeline. It is the series of steps involved in building any NLP model. These steps are common in every NLP project, so it makes sense to study them in this chapter. Understanding some common procedures in any NLP pipeline will enable us to get started on any NLP problem encountered in the workplace. Laying out and developing a text-processing pipeline is seen as a starting point for any NLP application development process. In this chapter, we will learn about the various steps involved and how they play important roles in solving the NLP problem and we’ll see a few guidelines about when and how to use which step. In later chapters, we’ll discuss specific pipelines for various NLP tasks (e.g., Chapters 4–7)."


def remove_stop_digits(tokens):
    swords = set(stopwords.words("english"))
    return [
        token.lower()
        for token in tokens
        if token not in swords and not token.isdigit() and token not in punctuation
    ]


def preprocess_corups(texts):
    return [remove_stop_digits(word_tokenize(text)) for text in texts]


result = preprocess_corups(text)
