import spacy
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

if __name__ == '__main__':
    spacy_en = spacy.load('en')
    
    sentences = []
    with open('wiki.txt', 'r') as f:
        for row in f:
            sentences.append(row)
            
    processed_sentences = []
    for sentence in sentences:
        words = spacy_en(sentence)
        processed_sentences.append(' '.join([w.lemma_ for w in words if w.text not in stopwords.words('english')]))
    del sentences
    
    with open('wiki_processed.txt', 'w') as f:
        f.writelines(processed_sentences)