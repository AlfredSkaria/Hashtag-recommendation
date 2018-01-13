from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation) 
lemma = WordNetLemmatizer()

path = "output.txt"

def doc_com(path):
	fopen = open("prep.txt",'w')
	with open(path,'r') as f:
		content = f.read()
		stop_free = " ".join([i for i in content.lower().split() if i not in stop])
		punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    	normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
	for line in normalized:
		print normalized.split()  
		
		#fopen.write(str(normalized.split()))

doc_com(path)


	

