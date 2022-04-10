from pyairtable import Table

from datetime import datetime

import traceback
import configparser
import requests


config = configparser.ConfigParser()
config.read('config.cfg')

# Airtable 
at_table_name = config.get('AIRTABLE', 'TABLE_NAME')
at_base_id = config.get('AIRTABLE', 'BASE_ID')
at_api_key = config.get('AIRTABLE', 'API_KEY')

# Quicket 
quicket_base_url = config.get('QUICKET', 'BASE_URL')
quicket_api_key = config.get('QUICKET', 'API_KEY')

today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

class airtableSync:
	def __init__(self, record_id, table_name = at_table_name):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(at_base_id, self.table_name, api_key=at_api_key)


class Quicket:
	def __init__(self, base_url = quicket_base_url, api_key = quicket_api_key):
		self.base_url = base_url
		self.api_key  = api_key

	def get_events(self, pageSize, lastModified = today):
		url = f"{self.base_url}?api_key={self.api_key}&pageSize=1&page=1&lastModified={lastModified}"

		payload = {}
		headers = {}

		response = requests.request("GET", url, headers=headers, data=payload)

		return response.text


# Quicket tets

p1 = Quicket(quicket_base_url, quicket_api_key)

results = p1.get_events(10)

print(f"Events: {results}")

# AT test

# table = Table(at_api_key, at_base_id, at_table_name)
# results = table.all()

# print(results)

