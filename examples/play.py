"""


based on work from: https://github.com/RobSpectre/Talks/tree/master/SMS%20For%20Humans:%20Using%20NLP%20and%20Python%20To%20Build%20Text%20Interfaces%20Fat%20Fingers%20Can%20Use
"""


from __future__ import print_function

from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import sys

lmtzr = WordNetLemmatizer()

for line in sys.stdin.readlines():
    blob = TextBlob(line.strip())

    sys.stdout.write("Detected language: {}\n".format(blob.detect_language()))
    sys.stdout.write("This message had {} words.\n".format(len(blob.words)))
    sys.stdout.write("Corrected sentence\n{}\n".format(blob.lower().correct()))
    proper_nouns = [tag[0] for tag in blob.tags if tag[1] == 'NNP']
    verbs = [lmtzr.lemmatize(tag[0], 'v') for tag in blob.tags if 'V' in tag[1]]
    sys.stdout.write("I found these proper nouns: {}\n".format(proper_nouns))
    sys.stdout.write("I found these verbs: {}\n".format(verbs))

    sentiment = blob.sentiment
    sys.stdout.write("Sentiment for that message: {}\n".format(sentiment))
    if sentiment.polarity > 0 and sentiment.subjectivity > 0.7:
        sys.stdout.write("That sounds amazing!\n")
    elif sentiment.polarity < 0 and sentiment.subjectivity > 0.7:
        sys.stdout.write("It'll get better.\n")
    else:
        sys.stdout.write("Meh.\n")

    sys.stdout.flush()
