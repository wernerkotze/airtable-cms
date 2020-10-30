from airtable import Airtable
from datetime import datetime

import os
import traceback

class Airtable:
	def __init__(self, record_id, table_name=os.getenv("AIRTABLE_TABLE_NAME")):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(os.getenv("AIRTABLE_BASE_ID"), table_name, api_key=os.getenv('AIRTABLE_API_KEY'))

	def get_campaign_id(self):
		record = airtable.get(self.record_id)

# set variables
campaign_id = ""
record_id   = ""

p1 = Airtable(campaign_id, record_id)

record = p1.get_record()

print(f"Record: {record}")