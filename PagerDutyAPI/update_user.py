#!/usr/bin/env python

import requests
import json
import csv

name = []
uid = []
email = []

#Parsing Function
def parse_csv():
	#Open CSV File
	with open('PagerDuty_Emails.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		#Skip the first row
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			#Go through each row and grab each column value
			else:
				name.append(row[0])
				uid.append(row[1])
				email.append(row[2])
				line_count += 1
#Update User Function
def update_user():
	i = 0
	#While loop to go through each user and update
	while i < len(uid):
		#Concatenate each UID to the API URL
		url = 'https://api.pagerduty.com/users/' + uid[i]
		#Standard PagerDuty API headers
		headers = {
			'Accept': 'application/vnd.pagerduty+json;version=2',
			'Authorization': 'Token token=#Put your token here',
			'Content-type': 'application/json'
			}
		#Payload to update specific email
		payload = {
			'user': {
				'email': email[i],
			}
		}
		#Actual request to update. Not sure if it needs to be a variable
		r = requests.put(url, headers=headers, data=json.dumps(payload))
		print(name[i],'has been successfully updated')
		i += 1
parse_csv()
update_user()
