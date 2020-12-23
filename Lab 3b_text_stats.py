import sys
import os.path
import re
import nltk
from nltk.corpus import stopwords

stpw=stopwords.words('english')

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


def remove(words):

	new_words = [wd for wd in words if wd not in stpw]

	return(new_words)

def split(words):
	res=[]
	#text = re.sub("1234567890!@#$%^&*()_+-=?`~\"\':;<,>\.\n"," ",text)
	for i in words:
		i=i.replace("?"," ").replace("."," ").replace(","," ").replace("!"," ").replace("#"," ").replace("\\"," ").replace("\n"," ")
		i=i.replace("@"," ").replace("^"," ").replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace("\""," ")
		i=i.replace("\'"," ").replace(";"," ").replace(":"," ").replace("{", " ").replace("}"," ").replace("\/"," ").replace("-"," ")
		i=i.replace("_"," ").replace("0"," ").replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ")
		i=i.replace("&"," ").replace("'"," ").replace("*"," ").replace("9"," ").replace("8"," ").replace("7"," ").replace("6"," ")
		if i != "":
			i = i.lower().split(" ")
			# delete space in the list
			i = filter(None, i) 
			res.extend(i)
	return(res)

def count(words):
	wordfreq = []
	[wordfreq.append(words.count(w)) for w in words]
	wordfreq = list(set(zip(words, wordfreq)))
	wordfreq = sorted(wordfreq,key = lambda x: x[1],reverse=True)
	return(wordfreq)



def result(words,wordfreq):
	print("The five most frequent words and three most frequent following words are shown as follow:\n")
	for i in range(5):
		wr = wordfreq[i][0]
		fr = wordfreq[i][1]
		print(wr,"(",fr,"occurrences )")
		nextwrind=[]
		for n,x in enumerate(words):
			if x==wr: nextwrind.append(n+1)
		nextwr = [words[m] for m in nextwrind]
		freqnextwr = count(nextwr)[:3]
		for p in freqnextwr:
			print("----",p[0],"(",p[1],")")
		print("\n")



def main():
	data=readfile()
	data=split(data)
	text=remove(data)
	c=count(text)
	result(text,c)




if __name__ == '__main__':

	main()





#Answer to the further question:
#1. In what way did you "clean up" or divide up the text into words (in the program; the text files should be 
#left unaffected)? This does not have to be perfect in any sense, but it should at least avoid counting "lord",
# "Lord" and "lord." as different words.

# In the split() function, we go through the words one by one, and use lower() function to change captial letter to lowercase. And save it to list. 

#2.Which data structures have you used (such as lists, tuples, dictionaries, sets, ...)? Why does that choice
# make sense? You do not have to do any extensive research on the topics, or try to find exotic modern data structures,
# but you should reflect on which of the standard data types (or variants thereof) make sense. If you have tried some 
#other solution and updated your code later on, feel free to discuss the effects!

#I mainly use lists in this py file, it is convient to use in this task, and it do not need much complex usage. So it makes sence to use list here.
#But in the second task I use a little dictionary to finish that. because dictionary have more convient to search and call the paired data.


















