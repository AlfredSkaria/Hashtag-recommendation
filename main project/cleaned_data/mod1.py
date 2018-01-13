from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize,sent_tokenize
en_stop = get_stop_words('en')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
stopn = []
stopped = []
fout = open("prep.txt",'w')
fin = open("prep.txt",'r') 
fout1 = open("data_prep_new.txt",'w')
fin1 = open("data_prep.txt",'r')
with open("out.txt",'r') as f:
		content = f.read()

for thing in en_stop:
	stopn.append(thing.encode("utf-8")) 

for line in content:
	if line not in exclude:
		fout.write(line)


for line in fin:
	for i in line.split():
		if i.lower() not in stopn:
			stopped = lemma.lemmatize(i)
			raw = stopped.lower()
			tokens = word_tokenize(raw)
			uni = tokens[0].encode('utf-8')+" "
			tok = sent_tokenize(uni)
			fout1.write(str(tok))
	fout1.write('\n')









# for line in fin:
# 	tok = sent_tokenize(line)
# 	fout1.write(tok)

# for item in fin:
# 	tok.append(item.encode("utf-8"))
# fout1.write(str(tok))
#print type(tokens)

#stopped = [line for line  in content1.lower().split() if not line in en_stop]
#stop_free = " ".join([i for i in content.lower().split() if i not in stop])
#punc_free = " ".join(ch for ch in content.lower().split() if ch not in exclude)
#normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
#raw = normalized.lower()
#tokens = word_tokenize(raw)
#print raw

