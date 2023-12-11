import pickle
def read_dictionary():
    with open('vocabulary.pkl', 'rb') as handle:
        dictionary = pickle.load(handle)
        dictionary = dict(sorted(dictionary.items()))


    return dictionary
