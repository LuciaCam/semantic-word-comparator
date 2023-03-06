from stopwords import *
import re
import math


def read_reference_text(filename: str) -> list[list[str]]:
    """
    This function takes a text file input and creates a list. Each element of this list is a sentence of the text file
    and the sentence itself is a list which contains each word of the sentence as individual strings.
    Punctuation is removed and all words are lowercase.

    :param: filename: it is the name of the text file, e.g. "example.txt". It should be a non-empty string, and the file
    should be stored in the project's environment.
    :return: text is a list of lists which all contain strings. Each string should only contain lowercase letters and
    numbers.
    """
    # opening the file
    text = open(filename)
    # reading the file as a string
    text = text.read()
    # splitting the file at each new line, creating a list of strings, where each string is a sentence
    text = text.split("\n")

    # for each sentence i:
    for i in range(len(text)):
        # we split the sentence into a list of words, using punctuations to cut between words
        text[i] = re.split("[ ,;:\'\"\?!]+", text[i])
        # we convert each word j of sentence i into lowercase
        for j in range(len(text[i])):
            text[i][j] = text[i][j].lower()
    return text


def make_word_vector(word: str, text: list[list[str]]) -> dict[str, int]:
    """
    This function takes a WORD and a TEXT and will return how many times a word that is in the same sentence as the
    chosen WORD inside our TEXT is present. This result will be given as a dictionary, where keys are words in the same
    sentences as WORD and the values are integers, representing how many times we found the key word.

    :param: word: word must be a lowercase word. For the semantic vector to have a meaning, word shouldn't be a
    stopword, however the function will still work even if it is.
    :param: text: text should be a list of lists which all contain strings. Each string should only contain lowercase
    letters and numbers.
    :return: vector will be a dictionary which contains words (lowercase letters and numbers) as keys and integers >= 1
    as values.
    """
    # creating an empty list which will contain the sentences with the word of interest in them
    sentences = list()
    # iterating over all sentences
    for i in range(len(text)):
        # checking if word is in sentence
        if word in text[i]:
            # adding sentence to our sentences list
            sentences.append(text[i])

    # creating empty dictionary which will be our vector
    vector = {}
    # iterating over sentences
    for i in range(len(sentences)):
        # iterating over each word w in sentence
        for w in sentences[i]:
            # checking that w isn't equal to our selected word, w isn't a stopword and is of length > 2
            if w != word and w not in stopwords and len(w) > 2:
                # if w already in vector dictionary, incrementing the value of w by 1
                if w in vector:
                    vector[w] = vector[w] + 1
                # if w isn't in vector dictionary, creating an entry with value 1
                else:
                    vector[w] = 1
    return vector


def scalar_product(v1: dict[str, int], v2: dict[str, int]) -> float:
    """
    This function computes the scalar product between two dictionaries by multiplying values which have the same keys
    in the two dictionaries together and then summing all of these products.

    :param: v1: the keys of v1 should be strings in the context of this exercise. However, the scalar_product can be
    generalized to take any type of keys. The important condition is that all values of v1 are numbers (floats or ints)
    :param: v2: same conditions as v1.
    :return: sp will be a float. It can be any real number.
    """
    # initiating scalar product as 0
    sp = 0.0
    # iterating over words of 1st dictionary
    for word in v1:
        # v2.get(word, 0) gets the value of word in v2 if it exists, or returns 0 if word isn't in v2
        sp = sp + v1[word] * v2.get(word, 0)
    return sp


def sim_word_vec(v1: dict[str, int], v2: dict[str, int]) -> float:
    """
    this function computes the cosine similarity between two dictionaries (called vectors).

    :param: v1: the keys of v1 should be strings in the context of this exercise. However, the scalar_product can be
    generalized to take any type of keys. The important condition is that all values of v1 are numbers (floats or ints).
    v1 must be non-empty and at least one value of v1 must be non-zero, otherwise there will be a division by zero in
    the formula, resulting in an error.
    :param: v2: same conditions as v1.
    :return: cos_sim is a float. As it is the cosine of an angle, its value will be between -1 and +1. If v1 = v2,
    cos_sim will be 1.
    """
    # using the formula for cosine similarity, the cosine of the angle between v1 and v2 is equal to:
    cos_sim = scalar_product(v1, v2) / (math.sqrt(scalar_product(v1, v1) * scalar_product(v2, v2)))
    return cos_sim
