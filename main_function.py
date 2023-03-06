from functions import *


def semantic_word_comparator(filename: str, word_list: list[str]) -> dict[str: dict[str: float]]:
    """
    This function takes a text file and a list of words. It returns a dictionary which for each word from the list (key)
    gives the closest word from the list semantically, as well as the cosine similarity between the two words.
    The choice of the closest word and the computation of the cosine similarity are based on the text file.
    :param filename: it is the name of the text file, e.g. "example.txt". It should be a non-empty string, and the file
    should be stored in the project's environment.
    :param word_list: the list should include only strings of lowercase letters and numbers, and each word should be
    present inside the text file.
    :return: similarities is a dictionary which has the strings of word_list as keys, and dictionaries as values. Each
    dictionary value is a dictionary containing only one key-value pair, with the key being the closest word to the key
    of the small dict, and the value the cosine similarity between the key of the small dict and the closest word.
    """
    # getting the text with our first homemade function
    text = read_reference_text(filename)

    # creating an empty dict which will contain each word of word list as key, and the vector of the word as value
    words_vectors = {}
    # filling the dictionary as mentioned above, using our second homemade function
    for word in word_list:
        words_vectors[word] = make_word_vector(word, text)

    # creating an empty dict which will contain each word from word list as key, and as value a dictionary containing
    # the closest word semantically, with the value of cosine similarity between them
    similarities = {}
    # iterating over words_vectors
    for word1 in words_vectors:
        # we create a temporary dict which will be used to store all words except word1 from the word list, and their
        # similarity score with respect to word1
        sim_dic = {}
        for word2 in words_vectors:
            if word1 != word2:
                # we use our third homemade function to compute the cosine similarity
                sim_dic[word2] = sim_word_vec(words_vectors[word1], words_vectors[word2])
        # once sim_dic is created, we retrieve the key which has the maximum value in sim_dic, using the parameter
        # key to designate the get function, which "gets" the values from a dictionary. The max will compare values of
        # the dictionary this way and return the key corresponding to the max value
        sim_max = max(sim_dic, key=sim_dic.get)
        # we create an entry in our similarities dict which to word1 (key) makes correspond the closest word
        # semantically (sim_max) and its cosine similarity score, retrieved from sim_dic
        similarities[word1] = {sim_max: sim_dic[sim_max]}

    return similarities
