import nltk
import docx2txt
import tkinter
import re
def findName(text):
	for i in text.split('\n'):
		if len(i.split())>=2 and len(i.split())<=4:
			return i
	return
def findMobile(text):
	return re.findall('[0-9]{10,13}', text)

def findEmail(text):
	return re.findall(r'\w+@\w+.\w+\.*\w*', text)

def findData(key, text):
	key.lower(), text.lower()
	KEY, TEXT = len(key), len(text)
	for i in text.split('\n'):
		print(i)


text = docx2txt.process('resume.docx').replace('\t', '\n')
worddict = {}
worddict['Name'] = findName(text)
worddict['Mobile'] = findMobile(text)
worddict['Email'] = findEmail(text)

print(worddict)
text = re.sub('([ ]{2,})', ' ', text)
wordlist=[]
for i in text.split('\n'):
	if len(i.split())>=1:
		wordlist.append(i)

