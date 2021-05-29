Movie-Genre_Sentiment-Analysis is a Django based project used to 
  1. Predict the genre of the movie and 
  2. Analyse the sentiment of the comment given to the movie


**Cosine similarity is used to find the genre**

**Using Scipy**
scipy.spatial.distance.cosine(u, v, w=None)


**Textblob is used to find the sentiment score**

  from textblob import TextBlob
  c = TextBlob(comment)
  sentiment_score =c.sentiment[0]
  
For reference: https://textblob.readthedocs.io/en/dev/quickstart.html

