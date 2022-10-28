# learning about the rapid extraction algorithm....
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from requests_html import HTMLSession
from rake_nltk import Rake 
def extract_text():
    s=HTMLSession()
    url="https://www.britannica.com/topic/homicide"
    response=s.get(url)
    return response.html.find('section#ref1',first=True).text
# print(extract_text())
r=Rake()
r.extract_keywords_from_text(extract_text())
for rating ,keyword in r.get_ranked_phrases_with_scores():
  if rating>5:
    print(int(rating),keyword)