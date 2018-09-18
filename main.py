import docx2txt
import re
import os

datatoProcess = {}
datatoProcess['Skills'] = ['technical skills', 'skills', 'technologies', 'programming languages', 'programming language', 'profile', 'summary', 'technology used', 'tools and software']
datatoProcess['Objective'] = ['objective']
datatoProcess['Education'] = ['educational qualifications', 'academic qualifications', 'academics', 'qualifications', 'qualification']
datatoProcess['Experience'] = ['experince', 'work experience', 'professional experince', 'total experince']

'''
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
'''
def process(text):
    Set, MainSet = set([]), {}
    for iterate in text:
        name = re.findall(r'([A-Za-z]*) ?([A-Za-z]+.{0,1}) ([A-Za-z])*', iterate)
        if len(name)>=1 and len(name)<=4:
            MainSet['Name'] = iterate
            break
        

    for iterate in text:
        mob = re.findall(r"\+{0,1}\d{2,3}\W{0,1}\d{3,4}\W{0,1}\d{3,4}\W{0,4}\d{3,4}", iterate)
        if mob>[]:
            MainSet['Mobile'] = mob
            break
        

    for iterate in text:
        email =  re.findall(r"([a-zA-Z0-9._ ]+[@][a-z]+[.]{1}[a-z]{2,5})", iterate)
        if email>[]:
            MainSet['Email'] = email
            break
    

    for iterate in text:
        if re.search(r'(Birth|DOB|Dob|dob)', iterate):
            dob =  re.findall(r"\d{2,4}\W\d{1,2}\W\d{2,4}", iterate)
            if dob>[]:
                MainSet['Date of Birth'] = dob
            break
    '''
    for Iterator in text:
        for key in datatoProcess: 
            for keyIterator in datatoProcess[key]:
                result = customRegex(keyIterator, Iterator)
                if result is not None:
                    for i in result.replace(',', ' ').split():
                        Set.add(i)
                    #resultSet[key] = Set
                    if key in MainSet:
                        MainSet[key].update((Set))
                    MainSet[key] = (Set)                       
                    Set.clear()
    ###resultSet['Mobile'] = findMob(listOfText)
    #print(findEmail(listOfText))'''
    return MainSet


for root, dirs, files in os.walk('../CVs/', topdown=False):
    ct=1
    for iterate in files:
        if iterate.split('.')[-1]=='docx' and iterate[0]!='~':
            print(iterate)
            name = '../CVs/'+iterate
            text = docx2txt.process(name).replace('\t', '\n')
            
            text = re.sub('CV', '', text)
            text = re.sub('Curriculum Vitae', '', text)
            text = re.sub('CURRICULUM VITAE', '', text)
            text = re.sub('CURRICULUM-VITAE', '', text)
            text = re.sub('RESUME', '', text)
            text = re.sub('Resume', '', text)
            text = re.sub('Gold medalist', '', text)
            text = re.sub('DR.', '', text)
            text = re.sub('Dr.', '', text)
            text = re.sub('Mr.', '', text)
            text = text.split('\n')
            print(ct, ':', process(text))
            ct+=1