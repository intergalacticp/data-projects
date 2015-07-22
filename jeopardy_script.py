import json
import operator

with open('jeopardy_questions.json') as data_file:
	data = json.load(data_file)

words = {}
wordtotals = {}
for line in data:
	question_words = line['question'].split(' ')
	answer = line['answer'].lower()
	for word in question_words:
		word = word.lower()
		if word in words:
			wordanswers = words[word]
			wordtotals[word] += 1
			if answer in wordanswers:
				wordanswers[answer] += 1
			else:
				wordanswers[answer] = 1
		else:
			words[word] = {answer:1}
			wordtotals[word] = 1

pairs = {}
for word in words:
	total = wordtotals[word]
	for answer in words[word]:
		answertotal = words[word][answer]
		percentage = float(answertotal)/float(total)
		pairs[word+': '+answer] = percentage

sorted_pairs = sorted(pairs.items(), key=operator.itemgetter(1),reverse=True)

pairechos = 0
for pair in sorted_pairs:
	if pair[1]!=1.0:
		print pair[0]
		print pair[1]
		pairechos+=1
	if(pairechos>50):
		break
