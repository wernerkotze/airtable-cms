from airtable import Airtable
from datetime import datetime

import os
import traceback
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

# Airtable Variables 
at_table_name = config.get('AIRTABLE', 'AIRTABLE_TABLE_NAME')
at_base_id = config.get('AIRTABLE', 'AIRTABLE_BASE_ID')
at_api_key = config.get('AIRTABLE', 'AIRTABLE_API_KEY')

class Airtable:
	def __init__(self, record_id, table_name = at_table_name):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(at_base_id, table_name, api_key=at_api_key)

	def get_campaign_id(self):
		record = self.at_instance().get(self.record_id)

# # set variables
# record_id  = "recDE4SwTI2fI9Lqh"
# table_name= "Broad"

# p1 = Airtable(record_id)

# campaign_id = p1.get_campaign_id()

# print(f"Campaign ID: {campaign_id}")
print(os.environ)