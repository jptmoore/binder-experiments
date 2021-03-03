import pandas as pd
import spacy
from functools import reduce
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def join_strings(x, y):
    return x + " " + y


def read_chunk(fname, chunk=100, rows=1000):
    df = pd.read_csv(fname, header=None, skiprows=1, chunksize=chunk, nrows=rows)
    return df


def extract_orgs(doc):
    for entity in doc.ents:
        if entity.label_ == "ORG":
            orgs.append(entity.text)


def process(chunk):
    for df in chunk:
        text = reduce(join_strings, df[10])
        doc = nlp(text)
        extract_orgs(doc)


orgs = []

nlp = spacy.load("en_core_web_sm")

chunk = read_chunk("../data/amazon_reviews_sample.csv")
process(chunk)

text = reduce(join_strings, orgs)
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
