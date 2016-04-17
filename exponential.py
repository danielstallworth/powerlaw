

""" Seeks to look at a hypothesis that new information acquired leads to exponential discoveries
	Logically any new discovery should be linearly correlated with the frequency of which that thing occurs in real life.
	To limit the scope and complexity, I look at frequency of words in a piece of text and then plotting out the histogram, not caring about gerunds, etc for now.
	Second step is to look at a more complicated problem from a top down approach: Starting with some complex code, break it apart to find the individual pieces, then see how many separate concepts you would need to know in order to reproduce the code. Can you understand it with only learning a small amount of coding concepts? How much do you need to learn?
"""

# Imports
from collections import Counter
import re

def word_counter(filename):
	# Read in the text
	word_dict = Counter()
	with open(filename) as f:
		# Get counts of each word in the text
		for line in f:
			word_dict.update(x.lower() for x in re.findall(r'\b\w+\b',line))
	word_list = []
	total_sum = 0
	for key,value in word_dict.items():
		if value > 50:
			word_list.append((key,value))
			total_sum = total_sum + value
	return word_list, total_sum

filename = raw_input("Name of the file? ")
print(word_counter(filename))
# print(total_sum)

