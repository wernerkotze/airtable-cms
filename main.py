from pyairtable import Table

from datetime import datetime

import traceback
import configparser
import requests

config = configparser.ConfigParser()
config.read('config.cfg')

# Airtable Variables
at_table_name = config.get('AIRTABLE', 'TABLE_NAME')
at_base_id = config.get('AIRTABLE', 'BASE_ID')
at_api_key = config.get('AIRTABLE', 'API_KEY')

class airtableSync:
	def __init__(self, record_id, table_name = at_table_name):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(at_base_id, self.table_name, api_key=at_api_key)

table = Table(at_api_key, at_base_id, at_table_name)
results = table.all()

print(results)

