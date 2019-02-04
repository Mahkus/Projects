#!/usr/bin/env python

import requests
import json

service_name_enabled = []
service_name_disabled = []
service_id = []

#Function to get PD Service info
def getService():
	#Specific URL query for individual Escalation Policy I was looking for
	url = 'https://api.pagerduty.com/escalation_policies?query=CORE%20Escalation&include%5B%5D=services&sort_by=name'
	headers = {
		'Accept' : 'application/vnd.pagerduty+json;version=2',
		'Authorization' : 'Token token=#Put your token here'
	}
	#Get request
	r = requests.get(url, headers = headers)
	data = r.json()
	#First loop into JSON
	for x in data['escalation_policies']:
		#Second loop into JSON
		for y in x['services']:
			#Grab the Service ID
			service_id.append(y['id'])
			#Check if the service is disabled or enabled
			if y['status'] == 'disabled':
				service_name_disabled.append(y['name'])
			else:
				service_name_enabled.append(y['name'])
#Function to update the Services to point to new Escalation Policy
def updateService():
	i = 0
	#While loop through my service_id array
	while i < len(service_id):
		#Concatenate the id to the end of the api URL
		url = 'https://api.pagerduty.com/services/' + service_id[i]
		print(url)
		headers = {
			"Content-Type": "application/json",
			"Accept": "application/vnd.pagerduty+json;version=2",
			"Authorization": "Token token=#Put your token here"
		}
		#Specific payload to put to the service
		payload = {
			'escalation_policy': {
				'id': 'PLOI1O7',
				'type': 'escalation_policy'
			}
		}
		r = requests.put(url, headers = headers, data = json.dumps(payload))
		print(r)
		print(i)
		i += 1

getService()
updateService()
