import chat_get
common_words = ["the", "are", "is", "be" , "to" , "of" , "and" , "a" , "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about",
"who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know",  "take",  "into", "year", "your", "some", "could", "them", "see", "other", "than", "then", "now", "only", "its" , "over", "also", "use", "two", "how", "our", "first", "well", "way", "even", "new", "want",
 "because", "any", "these" ,"give", "day" ,"most" ,"us"]


def belong(word, listOfWords):
	a = False;
	for i in range(len(listOfWords)):
		if (word == listOfWords[i]):
			a = True;
			break;
def remove_words(input, standard_words):
	modified_words = []
	for i in range(len(input)):
		if not belong(input[i], common_words):
			modified_words.append(input[i])
	return modified_words

def split_string(s): #To be called by main

	words = s.split()
	a = remove_words(words, common_words)

	temp_string = ""
	for x in a:
		temp_string+=str(x)+" "
	return temp_string
