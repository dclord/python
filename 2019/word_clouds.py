from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as numpy
import pandas as pd
from os import path
from PIL import Image

import matplotlib.pyplot as plt

df = pd.read_csv("data/wine/winemag-data-130k-v2.csv", index_col=0)
# NOTE Print dataset
#print(df.head())

# print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))
# print("There are {} types of wine in this dataset such as {}... \n".format(len(df.variety.unique()),", ".join(df.variety.unique()[0:5])))
# print("There are {} countries producing wine in this dataset such as {}... \n".format(len(df.country.unique()),", ".join(df.country.unique()[0:5])))
#

# NOTE Print Dataset by country, description and points
# print(df[["country", "description", "points"]].head())

# NOTE Group dataset by Country
country = df.groupby("country")

# NOTE Print dataset by country
# print(country.describe().head())

# NOTE Print top 5 average counteries
# print(country.mean().sort_values(by="points",ascending=False).head())

# NOTE Matplotlib Graph of top 5 countries
# plt.figure(figsize=(15,10))
# country.size().sort_values(ascending=False).plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Origin")
# plt.ylabel("No of Wines")
# plt.show()

# NOTE Highest ranking wines
# plt.figure(figsize=(15,10))
# country.max().sort_values(by="points", ascending=False)["points"].plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Origin")
# plt.ylabel("Highest ranking")
# plt.show()

# ----------------------------------------------------------------------------
# NOTE WordCloud
# Start with one review
# text = df.description[0]

# Join all descriptions
text = " ".join(review for review in df.description)
print("There are {} words in the combination of all review".format(len(text)))

# Stop words list
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavours"])

# Create wordcloud Image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# NOTE Save image to file
# wordcloud.to_file("data/wine/review.png")




