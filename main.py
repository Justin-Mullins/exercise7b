'''

Exercise 7b
Remove author names

In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.

'''
# Using this library to scrape text from artcles on the web.
from newspaper import Article
import nltk # For natural language processsing

nltk.download('punkt') 

url = input("Enter Url: ")

article = Article(url, language='en')

names = ['Ralph Waldo', 'Troy Beckert', 'Randy Thompson', 'Stella Draper', 'Clark Walsgrove']

article.download()
article.parse() # Parse article
article.nlp()  # Perform natural language processoring
text = article.text().split(' ')

word_count = 0
for name in names:
    if name.lower() in text.lower():
        text = text.replace(name, '_' * len(name))
    word_count += 1  

#To extract title
print("Article's Title:")
print(article.title)
print("")
 
#To extract text
print("Article's Text:")
print(article.text)
print("")
 
#To extract summary
print("Article's Summary:")
print(article.summary)
print("")