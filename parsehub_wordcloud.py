import sys
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

def generateWordCloud():	
	df = pd.read_csv("bleeping-hardware-results2.csv")

	stopwords = set(STOPWORDS)
	stopwords.update(["problem", "problems", "please", "help", "broken", "network", "confusion", "issue", "windows"])

	text = " ".join(title for title in df.post_name)

	text = text.lower()

	wordcloud = WordCloud(stopwords = stopwords).generate(text)

	# Display the generated image:
	# the matplotlib way:
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()

def main():
	generateWordCloud()

if __name__ == '__main__':
	main()