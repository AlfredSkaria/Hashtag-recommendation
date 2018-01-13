from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re
from nltk import word_tokenize
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()

path = "output.txt"
fout = open("data_prep.txt",'w')
def doc_proc(path):
	with open(path,'r') as f:
		content = f.read();
		for line in content:
			new_str = re.sub('[^a-zA-Z0-9\n\.]',' ',line)
			for item in new_str.split():
				if item not in stop:
					tokens = word_tokenize(new_str)
					#print tokens
					fout.write(str(tokens))






doc_proc(path)
#new_str = re.sub('[^a-zA-Z0-9\n.]','',line)
