import sys
import os.path
import re
import nltk
from nltk.corpus import stopwords
import random

#stpw=stopwords.words('english')

def readfile():
	try:
		filename=sys.argv[1]

		if not os.path.isfile(filename):
			print ( "We didn't find your file.")

		with open(filename) as file:
			data = file.readlines()
			print("we found your file",filename, ".\n")
		return (data)

	except IndexError:
		print ("Please give me a file name!")


#def remove(words):

#	new_words = [wd for wd in words if wd not in stpw]

#	return(new_words)

def split(words):
	res=[]
	#text = re.sub("1234567890!@#$%^&*()_+-=?`~\"\':;<,>\.\n"," ",text)
	for i in words:
		i=i.replace("#"," ").replace("\\"," ").replace("\n"," ")
		i=i.replace("@"," ").replace("^"," ").replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace("\""," ")
		i=i.replace("\'"," ").replace(";"," ").replace(":"," ").replace("{", " ").replace("}"," ").replace("\/"," ").replace("-"," ")
		i=i.replace("_"," ").replace("0"," ").replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ")
		i=i.replace("&"," ").replace("*"," ").replace("9"," ").replace("8"," ").replace("7"," ").replace("6"," ")
		i=i.replace(" "," ").replace("\n"," ").replace("."," ")
		if i != "":
			i = i.lower().split(" ")
			# delete space in the list
			i = filter(None, i) 
			res.extend(i)
	return(res)

def random_index(rate):
    start = 0
    randnum = random.randint(1, sum(rate))
    for index, item in enumerate(rate):
        start += item
        if randnum <= start:
            break
    return index

def count(words):
	wordfreq = []
	[wordfreq.append(words.count(w)) for w in words]
	wordfreq = list(set(zip(words, wordfreq)))
	wordfreq = sorted(wordfreq,key = lambda x: x[1],reverse=True)
	return(wordfreq)



def nextword(words,wordfreq,rw):
	#print("The five most frequent words and three most frequent following words are shown as follow:\n")
	wfdict=dict(wordfreq)
	fr=wfdict[rw]
	nextwrind=[]
	for n,x in enumerate(words):
		if x==rw: nextwrind.append(n+1)
	if nextwrind is []:
		return(None)
	else:
		nextwr = [words[m] for m in nextwrind if m<len(words)]
		freqnextwrdict = dict(count(nextwr))
		fnwdkey = list(freqnextwrdict.keys())
		fnwdval = list(freqnextwrdict.values())
		nextword = fnwdkey[random_index(fnwdval)]
		return(nextword)
		#return(freqnextwrdict)



def write(words,wordfreq,rw,num):
	print("The generate text is:")
	print(rw+" ",end='')
	for i in range(num):
		rw = nextword(words,wordfreq,rw)
		if rw is None:
			break
		else:
			print(rw+" ",end='')
			i=i+1
	print(".\n")




def main():
	data=readfile()
	data=split(data)
	#data=remove(data)
	c=count(data)
	write(data,c,sys.argv[2],int(sys.argv[3]))
	#nextword(data,c,"thee")

	#print(sys.argv[2],type(sys.argv[3]))




if __name__ == '__main__':

	main()