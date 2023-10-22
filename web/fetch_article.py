# filename: fetch_article.py

from newspaper import Article

url = "https://www.amadorvalleytoday.org/32097/features/acing-mit-with-aryan-jain-23-acing-admissions-advice/"

# Use newspaper3k to parse the article
article = Article(url)
article.download()
article.parse()

# Print the article text
print(article.text)