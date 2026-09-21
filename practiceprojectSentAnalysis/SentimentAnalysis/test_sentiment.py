''' tests sentiment_analyzer.'''
from sentiment_analysis import sentiment_analyzer

response = sentiment_analyzer("woo")
label = response['label']
score = response['score']
print(f"Label: {label}")
print(type(label))
print(f"Score: {score}")
print(type(score))
