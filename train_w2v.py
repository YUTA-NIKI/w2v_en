import spacy
from gensim.models import word2vec
from multiprocessing import Pool

from tqdm import tqdm
import logging

def lemmatize(sentence):
    spacy_en = spacy.load('en')
    words = spacy_en(sentence)
    return ' '.join([w.lemma_ for w in words])

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    
    sentences = []
    with open('wiki.txt', 'r') as f:
        for row in f:
            sentences.append(row)
    print('Loading EnWiki Data Finished...')
    
    p = Pool(4)
    processed_sentences = p.map(lemmatize, sentences)
    p.close()
    p.join()
    
    print('Lemmatization Finished...')
    
    model = word2vec.Word2Vec(sentences, size=400, min_count=20, window=12, workers=4)
    model.save("./w2v_enwiki_d400_w12_w_lemmatization.model")