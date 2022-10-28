from newspaper import Article
import nltk

nltk.download('punkt')
print("Enter the url:")
url = input('')
print("\n*********************\n")
article = Article(url)
article.download()
article.parse()
author = article.authors
pub = article.publish_date
article.nlp()
keywords = article.keywords
summary = article.summary
print("Author of article :\n")
print(author)
print("\n**************\n")
print("keyword of articles:\n")
print(keywords)
print("summary of article:\n")
print("\n**************\n")
print(summary)
