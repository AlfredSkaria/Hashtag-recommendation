from gensim import models
from gensim import utils
from gensim.models import Doc2Vec
#import numpy
import gensim


path = "data_prep.txt"
def read_corpus(path):
# 	print "hello"
	with open(path,'r') as f:
		for i,line in enumerate(f):
			yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])
			#print gensim.utils.simple_preprocess(line)
		

train_corpus = list(read_corpus(path))
#print train_corpus[:2]
model = gensim.models.doc2vec.Doc2Vec(size=50,min_count=1,iter=55)
model.build_vocab(train_corpus)
model.train(train_corpus, total_examples=model.corpus_count, epochs=model.iter)
#print model.infer_vector([u'thanks', u'dan', u'it', u'was', u'awesome', u'just', u'had', u'the', u'leftovers', u'and', u'no', u'oven', u'fups'])
#print model.most_similar([u'awesome'])
#print model.infer_vector('hii')
# vect = []
fout = open("vector_stop.txt",'w')
#fout1 = open("tokens.txt",'w')
for line in train_corpus:
	#fout1.write(str(line))
	#print model.infer_vector(str(line))
	vect = model.infer_vector(str(line))
 	fout.write(str(vect))
 	#fout1.write('\n')
 	fout.write('\n')
# docvec = model.infer_vector(str([1]))
# print docvec