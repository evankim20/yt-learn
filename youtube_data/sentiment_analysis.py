"""
preprocesosr library:
  - urls, emojis, smileys, 


"""
from text_preprocessing import remove_punctuation, remove_whitespace, remove_stopword
from pandarallel import pandarallel
from textblob import TextBlob
from pprint import pprint
import preprocessor as p
import pandas as pd
import numpy as np

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

# allows for multiprocessing (simple API)
pandarallel.initialize()


def preprocess(comments_df):
    """ preprocess all comments for a video before performing sentiment analysis """

    # basic text transformations
    comments_df['comments'] = comments_df['comments'].parallel_apply(p.clean)
    comments_df['comments'] = comments_df['comments'].parallel_apply(str.lower)
    comments_df['comments'] = comments_df['comments'].parallel_apply(
        remove_punctuation)

    # remove all stop words
    comments_df['comments'] = comments_df['comments'].parallel_apply(lambda comment: ' '.join
                                                                     ([word for word in comment.split() if word not in stop]))

    return comments_df


def sentiment_score(comments_df):
    """ return a sentiment value from -1 to 1 (0 being neutral) """

    comments_df = preprocess(comments_df)
    comments_df['sentiment'] = comments_df['comments'].parallel_apply(
        lambda tweet: TextBlob(tweet).polarity)

    sentiment_score = np.round(np.mean(comments_df['sentiment']), 2)
    return sentiment_score
