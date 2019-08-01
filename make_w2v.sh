pip install --upgrade gensim
curl https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 -o data/enwiki-latest-pages-articles.xml.bz2
python WikiExtractor.py -o data/wikitext data/enwiki-latest-pages-articles.xml.bz2
find data/wikitext/ | grep wiki | awk '{system("cat "$0" >> wiki.txt")}'
python train_w2v.py