from bs4 import BeautifulSoup
import requests
from gensim.summarization import summarize
print("Get a Summary of an Article")
url = input("Type in article url: ")
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

headline = content.find('h1').get_text()

p_tags = content.findAll('p')
p_tags_text = []
for p in p_tags:
	p_tags_text.append(p.get_text().strip())
# Filter out sentences that contain newline characters '\n' or don't contain periods.
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in p_tags_text if not ']' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
# Combine list items into string.
article = ' '.join(sentence_list)
summary = summarize(article, ratio=0.3)
print()
print("Headline: "+headline+"\n")
print(summary+"\n")
print(f"Article Length: {len(article)}")
print(f"Summary Length: {len(summary)}")