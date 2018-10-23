from gensim.models import KeyedVectors
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import re


word = morph.parse('стеклами')[0]
inflected = word.inflect({'gent'})
print(inflected)
#w2v_fpath = "news_upos_cbow_600_2_2018.vec.gz"

#w2v = KeyedVectors.load_word2vec_format(w2v_fpath, binary=False, unicode_errors='ignore')
#w2v.init_sims(replace=True)

#for word, score in w2v.most_similar(positive=["многоэтажка_NOUN"], topn=5):
#    print(word, score)