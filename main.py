'''

Exercise 7b
Remove author names

In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.

'''

names = ['Ralph Waldo', 'Troy Beckart', 'Randy Thompson', 'Stella Draper', 'Clark Walsgrove']

test_article = 'This is a research article done by Randy Thompson, Stella Draper, and Clark Walssgrove. It is based on work already conducted by Ralph Waldo and Troy Beckart'

def remove_names(article, names):
    # article = article.split(' ')
    word_count = 0
    for name in names:
        if name in article:
            article = article.replace(name, '_' * len(name))
        word_count += 1
    return article

print(remove_names(test_article, names))