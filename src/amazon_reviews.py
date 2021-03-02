import pandas as pd
import spacy
from functools import reduce


def read_chunk(fname, chunk=100, rows=1000):
    df = pd.read_csv(fname, header=None, skiprows=1, chunksize=chunk, nrows=rows)
    return df


def extract_orgs(doc):
    for entity in doc.ents:
        if entity.label_ == "ORG":
            orgs.append(entity.text)


def process(chunk):
    for df in chunk:
        text = reduce(lambda x, y: x + " " + y, df[10])
        doc = nlp(text)
        extract_orgs(doc)


orgs = []

nlp = spacy.load("en_core_web_sm")

chunk = read_chunk("../data/amazon_reviews_sample.csv")
process(chunk)
