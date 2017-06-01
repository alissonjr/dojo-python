# -*- coding: utf-8 -*-

#external libraries
import requests
import sys
from bs4 import BeautifulSoup

# link para quebrar: http://stackoverflow.com/questions/tagged/python?sort=frequent&pageSize=15

print("Searching the page...")

# get the page
page = requests.get('http://stackoverflow.com/questions/tagged/python?sort=frequent&pageSize=15')

# stack the page
soup = BeautifulSoup(page.content, 'html.parser')


# get all divs with class question-summary
# here is the questions that we would like to get
infos = soup.find_all('div', class_='question-summary')

# case not found any question
if len(infos) == 0:
	sys.exit('Informações não encontradas')

# if not, continue...

# open a file called 'questions.txt'
f = open('questions.txt', 'a')

# start an array of questions
questions_quantity = 0

print("Get informations")

# walk by informations
for info in infos:
	# get title
	title = info.find('div', class_='summary').h3.get_text()
	# get answers quantity
	answers = info.find('strong').get_text()
	# get views
	views = info.find('div', class_='views').get_text()
	# get votes
	votes = info.find('div', class_='votes').strong.get_text()
	# get user that made de questions
	user = info.find('div', class_='user-details').find('a')
	# get tags of question
	tags = info.find('div', class_='tags').find_all('a', class_='post-tag')
	tags_text = []
	for tag in tags:
		tags_text.append(tag.get_text())

	# merge informations
	content_obg = { "title": title, "answers": answers, "views": views, "votes": votes, 'user_name': user, "tags": tags_text }

	# add a question to count
	questions_quantity += 1

	# write the question information inside de file
	f.write(str(content_obg) + '\n')

# show informations about the operation
print("*/*-------------------------------------*/*")
print("We found {} questions inside this page.".format(questions_quantity))
print("We wrote this in questions.txt")
print("*/*-------------------------------------*/*")

# close the file
f.close()
