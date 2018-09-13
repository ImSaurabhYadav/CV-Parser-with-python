import nltk
import docx2txt
import tkinter
import re
import string

def findName(text):
    for iterate in text:
        if len(iterate.split())>=1 and len(iterate.split())<=4:
            return iterate
def findMob(text):
    for iterate in text:
        mob = re.search(r"(\d{9,13})|(\+\d{10,14})|(\+\d{1,3}\-\d{8,11})|(\+\d{1,3}\-\d{2,4}\-\d{2,4}\-\d{2,4})", iterate)
        if mob is not None:
            return mob.group(0)
        
def findEmail(text):
    for iterate in text:
        email =  re.findall(r"([a-zA-Z0-9._ ]+[@]([a-z]+[.]{1}){1,2}[a-z]{2,5})", text)
        return email


#
def customRegex(first, second):
    second = second.lower()
    length1 = len(first)
    length2 = len(second)
    for i in range(length2 - length1):
        if second[i]==first[0]:
            if(first==second[i:i+length1]):
                i = i+length1
                string=''
                while i<length2-1:
                    string+=second[i+1]
                    i+=1
                return string


def processTheText(keys, listOfText):
    resultSet = {}
    Set = set([])
    for Iterator in listOfText:
        for key in keys: 
            for keyIterator in keys[key]:
                result = customRegex(keyIterator, Iterator)
                if result is not None:
                    for i in result.replace(',', ' ').split():
                        Set.add(i)
                    #resultSet[key] = Set
                    print(key)
                    print(Set)
                    Set.clear()
    ###resultSet['Mobile'] = findMob(listOfText)
    #print(findEmail(listOfText))
    return resultSet

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

text = docx2txt.process('../cvs/AnchitGupta.docx').replace('\t', '\n')
'''text = text.replace(':', ' ')
text = re.sub('CV', '', text)
text = re.sub('Curriculum Vitae', '', text)
text = re.sub('CURRICULUM VITAE', '', text)
text = re.sub('RESUME', '', text)
text = re.sub('Resume', '', text)'''
#text = re.sub(r"(\-)|(\:)", ' ', text)
#text = text.translate(string.punctuation)
text = nltk.tokenize.word_tokenize(text)
is_noun = lambda pos: pos[:2] == 'NN'
nouns = [word for (word, pos) in nltk.pos_tag(text) if is_noun(pos)] 
print(nouns)

'''
datatoProcess = {}
datatoProcess['Name'] = ['name']
datatoProcess['Skills'] = ['technical skills', 'skills', 'technologies', 'programming languages', 'programming language', 'profile', 'summary', 'technology used', 'tools and software']
datatoProcess['Objective'] = ['objective']
datatoProcess['Education'] = ['educational qualifications', 'academic qualifications', 'academics', 'qualifications', 'qualification']
datatoProcess['Experience'] = ['experince', 'work experience', 'professional experince', 'total experince']
datatoProcess['D-O-B'] = ['dob', 'date of birth']
#print(text)
resultSet = processTheText(datatoProcess, text)
print(resultSet)
'''