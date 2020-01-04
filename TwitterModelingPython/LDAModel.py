import nltk
import pandas as pd
import gensim
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *
import pickle
from multiprocessing import freeze_support
nltk.download('wordnet')

if __name__ == '__main__':
    # add freeze support for multiprocessing LDA Multicore
    freeze_support()

    # use porterstemmer as stemmer
    stemmer = PorterStemmer()


    # function for lemmatizing
    def lemmatize_stemming(text):
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


    # function for preprocessing a tweet
    def preprocess(text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3 and "http" not in token:
                result.append(lemmatize_stemming(token))
        return result


    # function for training the lda model
    def train_lda(bow_corpus, dictionary, filename):
        lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary)
        # save the trained lda model with pickle
        pickle.dump(lda_model, open(filename, 'wb'))


    def prepare_docs(documents_outside):
        # map a tweet to a processed tweet
        return documents_outside['tweet'].map(preprocess)

    def create_bow_corpus_dict(filename_bow, filename_dictionary):
        # read in the tweets
        df = pd.read_csv("tweets.csv", error_bad_lines=False)
        # add an index column
        df["index"] = df.index
        # make a copy of the dataframe
        documents = df.copy()
        print(len(documents))

        # map a tweet to a processed tweet
        processed_docs = prepare_docs(documents)
        # create a dictionary. Its keys are the indexes and the value are tokens.
        dictionary = gensim.corpora.Dictionary(processed_docs)
        # filter the dictionary. Remove a token if it is in less than 15 tweets and is in more than 0.5 documents.
        # Also keep only the first 50000 tokens.
        dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=50000)
        # For each tweet create a dictionary how many words and how many times those words appear.
        bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
        pickle.dump(bow_corpus, open(filename_bow, 'wb'))
        pickle.dump(dictionary, open(filename_dictionary, 'wb'))


    # set a file name for saving the trained lda model
    filename = 'lda_model.sav'
    filename_bow_corpus = 'bow_corpus.sav'
    filename_dict = 'dict.sav'

    # create the bow corpus and dictionary
    create_bow_corpus_dict(filename_bow_corpus, filename_dict)

    bow_corpus = pickle.load(open(filename_bow_corpus, 'rb'))
    dictionary = pickle.load(open(filename_dict, 'rb'))

    # train the model and save it
    train_lda(bow_corpus, dictionary, filename)

    # load the before saved model
    lda_model = pickle.load(open(filename, 'rb'))

    # test an unseen document and see how it scores on the topics
    unseen_document = 'I was going to the cinema and met a dog.'
    bow_vector = dictionary.doc2bow(preprocess(unseen_document))
    for index, score in sorted(lda_model[bow_vector], key=lambda tup: -1 * tup[1]):
        print("Score: {}\t Topic: {}".format(score, lda_model.print_topic(index, 10)))

