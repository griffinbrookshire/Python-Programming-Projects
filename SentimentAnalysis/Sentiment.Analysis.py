import csv
import matplotlib.pyplot as plt
import string

"""
Your code for part 1.
The idea is to make a list of positive and negative words from the lexicon files,
and simply count the occurences of positive and negative words in the text.
So in general, you should have the following steps:
1. Load the text
2. Load the lexicons
3. Count occurences
4. Plot histogram (make a reasonable size for the bins)

The following is a short script of loading the bb_2011_2013.csv file. Note that
bb_2011_2013.csv and bb_1996_2013.csv is a little different.

	with open('data/bb/bb_2011_2013.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')

"""


"Step 1: Load the text."


dataSmall = []
with open('data/bb/bb_2011_2013.csv', 'r') as dataFileSmall:
    reader = csv.reader(dataFileSmall, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        rowText = row[2].lower()
        dataSmall.append(rowText.split())

dataBig = []
with open('data/bb/bb_1996_2013.csv', 'r') as dataFileBig:
    reader = csv.reader(dataFileBig, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        rowText = row[4].lower()
        dataBig.append(rowText.split())


"Step 2: Load the lexicons."


posLex = []
with open('data/lexicons/lexicon.finance.positive.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        posLex.append(rowText)
with open('data/lexicons/lexicon.finance.positive.LoughranMcDonald.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        posLex.append(rowText)
with open('data/lexicons/lexicon.generic.positive.HuLiu.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        posLex.append(rowText)

negLex = []
with open('data/lexicons/lexicon.finance.negative.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        negLex.append(rowText)
with open('data/lexicons/lexicon.finance.negative.LoughranMcDonald.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        negLex.append(rowText)
with open('data/lexicons/lexicon.generic.negative.HuLiu.csv', 'r') as posLexFile:
    reader = csv.reader(posLexFile, delimiter=',', quotechar='"')
    for row in reader:
        rowText = row[0].lower().strip()
        negLex.append(rowText)


"Step 3: Count occurences."


def scoreSentiment(sentences, posLexicons, negLexicons):
    scores = []
    for record in sentences:
        score = 0
        for word in record:
            if word in posLexicons:
                score+=1
            if word in negLexicons:
                score-=1
        scores.append(score)
    return scores

smallScores = scoreSentiment(dataSmall, posLex, negLex)

bigScores = scoreSentiment(dataBig, posLex, negLex)


"Step 4: Plot histogram."


import numpy as np
y_pos = np.arange(len(smallScores))
plt.bar(y_pos, smallScores, align='center')
plt.ylabel('Sentiment Score')
plt.title('Small Data Sentiment Scores')
plt.show()

y_pos = np.arange(len(bigScores))
plt.bar(y_pos, bigScores, align='center')
plt.ylabel('Sentiment Score')
plt.title('Big Data Sentiment Scores')
plt.show()
