from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python"

html = urlopen(url).read()

soupified = BeautifulSoup(html, "html.parser")
question = soupified.find("div", {"id": "question-header"})
question_text = question.find("a", {"class": "question-hyperlink"})
print("Question: \n", question_text.get_text().strip())
