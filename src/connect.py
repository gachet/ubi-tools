import requests
import os

def post_var(token, ubi_source, ubi_var, value, timestamp=None, context=None):
	
	'''
	This function posts data to ubidots

	Input parameters:

	token: The Ubidots token
	ubi_source: The name of the user's Ubidots datasource
	ubi_var: The name of the user's Ubidots variable
	value: Value to be sent
	timestamp: Optional, for custom timestamp
	context: Optional, for custom context
	'''

	try:
		url = os.getenv("UBIDOTS_URL") if os.getenv("UBIDOTS_URL") is not None else "http://things.ubidots.com/"
		url = url + "api/v1.6/devices/" + ubi_source + "/"
		headers = {"X-Auth-Token": token,
					"Content-Type":"application/json"}
		data = {ubi_var:{"value": value}}
		if (timestamp!=None):
			data[ubi_var]["timestamp"]=timestamp
		if (context!=None):
			data[ubi_var]["context"]=context
		r = requests.post(url=url, headers=headers, json= data)
	except Exception as e:
		return e

def get_var(token, ubi_source, ubi_var, value, timestamp=None, context=None):
	
	'''
	This function gets data from ubidots

	Input parameters:

	token: The Ubidots token
	ubi_source: The name of the user's Ubidots datasource
	ubi_var: The name of the user's Ubidots variable
	
	Return:

	Returns in this order the next parameters: value, timestamp, context
	'''

	try:
		url = os.getenv("UBIDOTS_URL") if os.getenv("UBIDOTS_URL") is not None else "http://things.ubidots.com/"
		url = url + "api/v1.6/devices/" + ubi_source + "/" + ubi_var + "/values?page_size=1"
 		headers = {"X-Auth-Token": token,
					"Content-Type":"application/json"}
		r = requests.get(url=url, headers=headers)
		return r.json()[0]['value'], r.json()[0]['timestamp'], r.json()[0]['context']
	except Exception as e:
		return e

