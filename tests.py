from main_function import *
import pprint
# pprint allows to print dictionaries' elements in columns instead of one very long line


TEST = ['canada', 'disaster', 'flood', 'car', 'road', 'train', 'rail', 'germany', 'switzerland', 'technology',
        'industry', 'conflict']

pprint.pprint(semantic_word_comparator("ref-sentences.txt", TEST))

TEXT = ['spain', 'anchovy', 'france', 'internet', 'china', 'mexico', 'fish', 'industry', 'agriculture', 'fishery',
        'tuna', 'transport', 'italy', 'web', 'communication', 'labour', 'fish', 'cod']

pprint.pprint(semantic_word_comparator("ref-sentences.txt", TEXT))
