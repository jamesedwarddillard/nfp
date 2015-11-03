""" logic for reading tweets and making them guesses """
import re

test_tweet = "-180K"

def guess_finder(tweet_text):
	best_guess = ''
	if numb_k_find(tweet_text):
		guess = numb_k_transform(tweet_text)
		best_guess = guess
	elif full_number_find(tweet_text):
		guess = full_number_transform(tweet_text)
		best_guess = guess
	else:
		best_guess = "Sorry, we didn't get that"
	negative = positive_or_negative(tweet_text)
	return best_guess * negative

def numb_k_find(tweet_text):
	searchObj = re.search('[0-9]*[K|k]', tweet_text, flags = 0)
	return searchObj

def numb_k_transform(tweet_text):
	# find the match
	searchObj = numb_k_find(tweet_text)
	match = searchObj.group()
	#identify the number
	number = re.search('[0-9]*', match, flags = 0)
	guess = number.group()
	guess = int(guess)*1000 
	return guess

def full_number_find(tweet_text):
	searchObj = re.search('[0-9]*[,]?[0-9]*[,]?[0-9]*[,]?[0-9]*', tweet_text, flags = 0)
	return searchObj

def full_number_transform(tweet_text):
	searchObj = full_number_find(tweet_text)
	match = searchObj.group()
	number = re.sub(r'\D', "", match)
	guess = int(number)
	return guess

def positive_or_negative(tweet_text):
	tweet_text = tweet_text.lower()
	negative = re.search('[lost]|[loses]|[-]', tweet_text, flags = 0)
	if negative:
		return -1
	else:
		return 1

